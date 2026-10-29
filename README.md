# jiangnan-fiction-craft

以江南小说精读证据为依据的中文小说写作参考库，支持查例、比较写法与适用条件，以及按需构思、续写和修改。当前版本 **0.19.5**：局部补充D4动作与心理分析、收窄P3因果表述，加入使用反馈入口和单题测评记录；保留已有分析和目录，不宣称写作效果提升。

已纳入《此间的少年》及后记、《龙族》六册、《九州·缥缈录》六册及《天之炽》两册，共189份章节分析、原89例细读、S1–S5五组句段分析、一条卷内关系线和[一段战役多线回读](references/techniques/multi-line-piaomiao-03.md)。逐卷范围、版本限制与来源见[书目索引](references/books/index.md)。

## 从哪里开始

| 用途 | 入口 |
|---|---|
| 让代理按当前任务使用本skill、交付前回看 | [SKILL.md](SKILL.md) |
| 按写作问题查例、找现稿的问题 | [cheatsheet.md](cheatsheet.md) |
| 比较相近写法和适用条件 | [patterns.md](patterns.md#comparisons) |
| 直接按语言、句段、描写、人物或情节查找 | [SKILL中的专题入口](SKILL.md#按需读取) |
| 按书查章节和证据 | [书目索引](references/books/index.md) |
| 理解术语 | [glossary.md](glossary.md) |
| 继续合入新书、核对来源或查看更新记录 | [来源与维护](references/maintenance/update.md) |

例如：

> 使用 jiangnan-fiction-craft 比较旧事放在动作前、回应后各有什么作用。给原文例子和适用条件，先不改稿。

> 使用 jiangnan-fiction-craft 评审这章小说。先找影响阅读最大的一至三个问题，再给局部修改稿；保留人物设定、既定视角和事实边界。

阅读材料按问题加载，不需要每次通读全部书目，也不把分析表或检查清单写进小说。

第一次使用可看[完整编辑示例](references/maintenance/usage-example.md)：从一段原创告别原稿出发，查两条材料，解释取舍，再给局部修改和未解决部分。这是AI 编写的演示，不是效果测评。

## 目录

```text
SKILL.md                  任务、交付方式、核心判断与专题入口
cheatsheet.md             按写作问题查找、修改取舍与交付说明
patterns.md               六组写法比较、九组原方法与证据入口
glossary.md               术语
chapters/                 189份章节分析；原文件名和编号保留
references/
  techniques/             语言、句段、描写、人物、情节、跨章与跨书分析
  books/                  书目总索引、逐卷索引及逐卷局部细读
  maintenance/            来源规则、安装验证、使用示例、更新记录及项目调研
sources/                  15份来源清单及《龙族》逐册状态
scripts/check_skill.py    无第三方依赖的结构检查
.github/workflows/        提交与 PR 的自动结构检查
LICENSE                   文字与脚本的许可范围
NOTICE                    小说引文与第三方材料声明
LICENSES/                 CC BY 4.0、MIT 完整条款
```

`SKILL.md`给出使用方式；`cheatsheet.md`集中具体问题；`patterns.md`比较方法；书目页负责定位原有分析。逐卷细读留在各书入口下，不把同一片段重复提炼成新的通用规则。

## 安装与验证（Codex）

先支持 Codex 的项目内安装。准备 Git，在你写作项目的根目录打开终端，运行：

```sh
mkdir -p .agents/skills
git clone --branch v0.19.5 --depth 1 https://github.com/SleepyLGod/jiangnan-fiction-craft-skill.git .agents/skills/jiangnan-fiction-craft
```

这会安装完整仓库及配套材料，保留相对路径。固定版本的克隆会提示处于 detached HEAD，这是按标签安装的正常状态；不要只复制 `SKILL.md`。若目标目录已存在，先确认其版本及有无自己的改动，不覆盖它。

在 Codex 中打开这个写作项目，检查 skill 选择列表中是否出现 `jiangnan-fiction-craft`，再显式调用：

> 使用 $jiangnan-fiction-craft，先读取它的 SKILL.md，再查人物 C1。告诉我该条目的相对路径、书源定位和一条适用边界。先不写小说；如果未找到，请直接说明。

预期找到 `references/techniques/close-reading-character.md` 的 C1，定位包含 `cijian:ch9:P0002–P0011`，并指出这一条不能把人物固定成永远相同的反应。回答里能复述 skill 名称不等于读到了文件：可查看读取记录，核对实际路径。未出现在列表时，检查目录中是否直接有 `SKILL.md`，并重启 Codex 后再看；避免同时放置多个同名副本。

只想核对安装文件且本机有 Python 3.10 或以上，可在写作项目根目录运行：

```sh
python3 .agents/skills/jiangnan-fiction-craft/scripts/check_skill.py
python3 -B -m unittest discover -s .agents/skills/jiangnan-fiction-craft/scripts -p test_check_skill.py
```

安装位置依据 [Codex 官方说明](https://learn.chatgpt.com/docs/build-skills)。此前的[安装验证记录](references/maintenance/installation.md)覆盖当时的公开仓库下载、文件完整性和 Codex 的 skill 发现，没有通过模型回答验证上述安装自查提问。后续写作比较另见[单题测评记录](references/maintenance/evaluation-2026-10-29.md)，不能替代安装验证。其他宿主、全局安装和桌面选择器的手动操作尚未验证。

## 使用边界

仓库包含分析、必要短引、来源指纹与覆盖记录，不包含小说全文、电子书、逐段reader或本机转换工作目录。原文锚点对应记录中的本地文字版本，不是纸书页码；版本未与指定纸本逐字校勘。

方法属于编辑归纳，不是作者自述理论，也不认证作者独有风格。本地样稿比较出现过局部差异、交付遗漏和评阅误判；广播站单题比较中，维护代理的编辑判断更倾向Terra不用库稿，尚未显示库的额外收益。具体材料、用量与限制见[单题测评记录](references/maintenance/evaluation-2026-10-29.md)；其中没有检验本版最后补充的D4操作提示，也不能据单题判断稳定改善或普遍无效。

跨章与多线研究目前有一条卷内关系线和一段战役，未补成整卷主次线篇幅安排、跨卷总伏笔表或完整人物生涯研究。漫画方法也尚未经过作品研究与验证。

## 使用反馈

欢迎[填写一次真实使用反馈](https://github.com/SleepyLGod/jiangnan-fiction-craft-skill/issues/new?template=usage-feedback.yml)，也可先[查看模板字段](.github/ISSUE_TEMPLATE/usage-feedback.yml)。有帮助、没有帮助或出错的经历都可以，不需要评分或为了反馈重跑任务。

先填版本与环境、原始任务、首次结果和具体得失；读取记录、可能归因及证据选填，不知道就保留未知。指出实际采用或拒绝的建议及原因，比“好用／不好用”更便于核对。后续重写另标轮次，不覆盖第一次结果。

内容、组织、模型执行与运行环境分开核对，表达偏好也可单独记录；表单中的分类只是猜测，维护时依据记录判断，不凭一次结果认定稳定问题。Issue 会公开，只分享愿意公开的稿件片段和脱敏记录。

## 许可

本项目按路径分别授权，具体范围见 [LICENSE](LICENSE)：

| 范围 | 许可 |
|---|---|
| 贡献者有权许可的文字、精读分析、方法说明与资料编排 | [CC BY 4.0 完整条款](LICENSES/CC-BY-4.0.txt) |
| `scripts/` 下的脚本、回归测试及 `.github/workflows/` 自动检查配置 | [MIT 完整条款](LICENSES/MIT.txt) |
| 小说引文和其他第三方受保护材料 | 不在上述授权范围内，见 [NOTICE](NOTICE) |

文字可按 CC BY 4.0 使用、修改和商用，需适当署名、链接许可并注明修改；脚本按 MIT 保留版权和许可声明。独立分析的许可不等于原著授权。本项目不声称获得原作作者、出版方或所调研项目的官方背书。

## 维护检查

在仓库根目录运行：

```sh
python3 scripts/check_skill.py
python3 -B -m unittest discover -s scripts -p test_check_skill.py
```

GitHub Actions 在提交到 `main`、提交 PR 或手动触发时运行同样两项命令，使用 Python 3.11，不调用模型；工作流只有仓库内容读取权限。

检查相对链接与章节锚点、书目可达性、来源定位边界、分析编号与清单对应、打包范围及许可文件是否齐全。许可文件检查不认证每处第三方引用的合法性，也不代替回读原文或实际写作比较。文件格式通过不表示文学效果通过。

文件范围遵循当前`.gitignore`中的文件名通配和目录排除，保留未提交的新分析；检查不依赖Git。若新增当前匹配器不支持的忽略语法，脚本会明确报错。发布文档不能链接到被排除的本地材料。

继续阅读新书或补充方法时，沿用[来源与维护](references/maintenance/update.md)中的证据约束，保留已有分析。文本提取使用[book-to-skill](https://github.com/virgiliojr94/book-to-skill)；其他项目调研保留在[独立备忘](references/maintenance/related-skills.md)。
