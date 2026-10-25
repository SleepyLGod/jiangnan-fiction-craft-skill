#!/usr/bin/env python3
"""Check local navigation, source bounds, and the distributable skill files."""

from __future__ import annotations

import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
CITATION = re.compile(
    r"\b(cijian|lz[124]|lz3[abc]|pm[1-6]|tz[12]):"
    r"(ch\d+|part\d{4}):P(\d{4})(?:[–-]P(\d{4}))?"
)


def heading_ids(text: str) -> set[str]:
    """Collect explicit anchors and GitHub-style IDs used by these documents."""
    ids = set(re.findall(r"<a\s+id=[\"']([^\"']+)", text))
    seen: Counter[str] = Counter()
    for title in re.findall(r"^#{1,6}\s+(.+)$", text, re.MULTILINE):
        title = re.sub(r"<[^>]+>|[*`~]", "", title).strip().lower()
        base = "".join(
            char
            for char in title
            if unicodedata.category(char)[0] in "LN" or char in "-_ "
        ).replace(" ", "-")
        suffix = f"-{seen[base]}" if seen[base] else ""
        ids.add(base + suffix)
        seen[base] += 1
    return ids


def check() -> dict[str, int]:
    """Raise ValueError on structural failures; return verified file counts."""
    errors: list[str] = []
    files = [
        path for path in ROOT.rglob("*")
        if path.is_file() and ".git" not in path.relative_to(ROOT).parts
    ]
    markdown = {path: path.read_text(encoding="utf-8") for path in files if path.suffix == ".md"}
    graph: dict[Path, set[Path]] = {path: set() for path in markdown}
    links = 0
    for path, text in markdown.items():
        for raw in LINK.findall(text):
            parsed = urlsplit(raw.strip().strip("<>"))
            if parsed.scheme or parsed.netloc:
                continue
            target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if not target.is_relative_to(ROOT) or not target.exists():
                errors.append(f"{path.relative_to(ROOT)}: missing or nonportable link {raw}")
                continue
            if parsed.fragment and target in markdown:
                if unquote(parsed.fragment) not in heading_ids(markdown[target]):
                    errors.append(f"{path.relative_to(ROOT)}: missing fragment {raw}")
            if target in markdown:
                graph[path].add(target)
            links += 1

    reachable: set[Path] = set()
    pending = [ROOT / "SKILL.md"]
    while pending:
        path = pending.pop()
        if path not in reachable:
            reachable.add(path)
            pending.extend(graph.get(path, set()))
    for path in markdown:
        if path.name != "README.md" and path not in reachable:
            errors.append(f"{path.relative_to(ROOT)}: unreachable from SKILL.md")

    chapters = {path.name for path in (ROOT / "chapters").glob("ch*.md")}
    numbers = sorted(int(re.match(r"ch(\d+)", name)[1]) for name in chapters)
    if not numbers or numbers != list(range(1, max(numbers) + 1)):
        errors.append("chapter numbers are missing or duplicated")
    registered = {name for name in chapters if re.fullmatch(r"ch\d+-cijian-.+\.md", name)}
    bounds: dict[tuple[str, str], int] = {}
    manifests = sorted((ROOT / "sources").glob("*-manifest.json"))
    for path in manifests:
        data = json.loads(path.read_text(encoding="utf-8"))
        source_id = data["source_id"]
        documents = data.get("documents", data.get("navigation", []))
        for doc in documents:
            stem = doc.get("stem", Path(doc["source"]).stem)
            bounds[source_id, stem] = doc["paragraphs"]
        analysis = data.get("analysis_files", [])
        for name in analysis:
            if name not in chapters:
                errors.append(f"{path.name}: missing analysis {name}")
            if name in registered:
                errors.append(f"{path.name}: analysis registered twice: {name}")
            registered.add(name)
    if registered != chapters:
        errors.append(f"unregistered analysis files: {sorted(chapters - registered)}")

    citations = 0
    for path, text in markdown.items():
        for source_id, stem, start, end in CITATION.findall(text):
            limit = bounds.get((source_id, stem))
            if limit is None or not 1 <= int(start) <= int(end or start) <= limit:
                errors.append(
                    f"{path.relative_to(ROOT)}: source bounds {source_id}:{stem}:P{start}–P{end or start}"
                )
            citations += 1

    allowed_roots = {"chapters", "references", "sources", "scripts"}
    allowed_top = {"SKILL.md", "README.md", "patterns.md", "cheatsheet.md", "glossary.md", ".gitignore"}
    for path in files:
        relative = path.relative_to(ROOT)
        if (len(relative.parts) == 1 and path.name not in allowed_top) or (
            len(relative.parts) > 1 and relative.parts[0] not in allowed_roots
        ) or path.suffix not in {".md", ".json", ".py", ""}:
            errors.append(f"unexpected packaged file: {relative}")
        if re.search(r"(?:/Users/|/private/|/tmp/|file://)", path.read_text(encoding="utf-8")):
            if relative != Path("scripts/check_skill.py"):
                errors.append(f"machine-specific path in {relative}")

    frontmatter = markdown[ROOT / "SKILL.md"].split("---", 2)
    if len(frontmatter) != 3 or not re.search(r"^name: jiangnan-fiction-craft$", frontmatter[1], re.MULTILINE):
        errors.append("SKILL.md name/frontmatter is invalid")
    if len(frontmatter) == 3 and not re.search(r"^description: .+", frontmatter[1], re.MULTILINE):
        errors.append("SKILL.md description is missing")
    for path in (ROOT / "sources").glob("*.json"):
        json.loads(path.read_text(encoding="utf-8"))
    if errors:
        raise ValueError("\n".join(errors))
    return {
        "files": len(files), "chapters": len(chapters), "manifests": len(manifests),
        "markdown_links": links, "full_source_anchors": citations,
    }


def main() -> int:
    """Report checks without claiming to validate literary effect or raw source text."""
    try:
        result = check()
    except (ValueError, KeyError, OSError) as exc:
        print(f"Skill check failed:\n{exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    print("Structure verified; original text and writing quality were not tested.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
