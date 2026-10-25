# 其他写作 Skill 调研备忘

调研日期：2026-10-24。

本文单独保存外部项目的定位、可参考设计和证据限制，供以后需要时查阅。当前继续建设 `jiangnan-fiction-craft`，不据此调整现有规则、安装其他 skill 或启动比较测试。

## 调研范围

核查了四个仓库的入口、部分研究笔记、写作工作流、测试材料，以及两个审计脚本的代码。没有执行这些 skill 或脚本，没有独立复算原始语料统计，也没有重跑盲测。下文区分仓库文件中的内容与我们的判断。

链接固定到本次核查的提交，后续仓库变化不自动更新本文。

| 项目 | 核查提交 | 主要定位 | 后续参考价值 |
|---|---|---|---|
| [tianyayu6/jiangnan-writer](https://github.com/tianyayu6/jiangnan-writer) | `35d5954a64ee343f8c0d7b4bb21e42f2da1324c7` | 原创小说与散文的构思、写作、修订 | 题材分流、长篇连续性、修订顺序 |
| [zuoyou12/longzu.skillls](https://github.com/zuoyou12/longzu.skillls) | `3f05bad7b6284c087f449d624fd6360f406e73f8` | 江南与烽火戏诸侯的风格练习及同人辅助 | 语言测量、采样记录、公开测试样本 |
| [cyberk1895/jiang-nan-skill](https://github.com/cyberk1895/jiang-nan-skill) | `d70c0ad03f4bd13dd1c5b77c82da832d80df0a15` | 作者角色扮演、创作诊断与思维顾问 | 访谈、文论、创作手记的资料线索 |
| [Carl24-star/jiang-nan-perspective](https://github.com/Carl24-star/jiang-nan-perspective) | `13fca1709b8a91072d1c4bb3de79052462fb23a7` | 文学、人物、IP与创作者困境分析 | 创作分析问题及观点适用条件 |

## 1. tianyayu6/jiangnan-writer

### 文件内容

- 主工作流是判断任务与题材、建立故事卡、选择少数叙事机制、写场景、检查连续性、修订。区分校园群像、都市幻想、历史史诗、关系武侠、都市科幻和回望散文。
- 长篇工作流包含章节承诺、角色能力与代价、角色知识、关系债务、制度与势力、物件与回声六类记录。
- 修订顺序先处理事实、连续性、人物选择和场景变化，再处理对话、意象和句子。
- 项目自述使用358个文本文件进行全库统计，并对代表文本结构精读。公开研究摘要记录了文体差异和统计局限。
- `audit_prose.py` 检查专名、套话、句长、词语密度及重复等表层信号，不检查动机或叙事因果是否成立。

### 我们的判断

这是四者中最适合对照原创写作流程的项目。尤其值得保留的是角色知识、能力限制与承诺回收等连续性记录，而非再增加一批叙事机制名称。

“评分达到15/20可交付”“每隔若干章回收承诺”等是项目设置的编辑约定，不能当成经过验证的文学规律。语料覆盖广的自述也不能直接证明生成效果优于其他方法。

来源：[入口](https://github.com/tianyayu6/jiangnan-writer/blob/35d5954a64ee343f8c0d7b4bb21e42f2da1324c7/SKILL.md)、[长篇工作流](https://github.com/tianyayu6/jiangnan-writer/blob/35d5954a64ee343f8c0d7b4bb21e42f2da1324c7/references/longform-workflow.md)、[质量量表](https://github.com/tianyayu6/jiangnan-writer/blob/35d5954a64ee343f8c0d7b4bb21e42f2da1324c7/references/quality-rubric.md)、[语料研究](https://github.com/tianyayu6/jiangnan-writer/blob/35d5954a64ee343f8c0d7b4bb21e42f2da1324c7/references/corpus-study.md)、[审计代码](https://github.com/tianyayu6/jiangnan-writer/blob/35d5954a64ee343f8c0d7b4bb21e42f2da1324c7/scripts/audit_prose.py)。

## 2. zuoyou12/longzu.skillls

### 文件内容

- 提供江南独立版、烽火独立版和融合版，区分共享叙事规则与按作者加载的语言规则。
- 项目自述对《龙族1—4》和《剑来》做全文统计，并记录45个精读采样点；江南模块另有六篇随笔的测量说明。
- 规则涉及对话动词、句段长度、标点、比喻标记、幽默和抒情方式，也包括“长辈给少年讲人生”等场景安排。
- `FIDELITY.md` 公开五段样本和评审摘要：四段按两种作者模式生成的短文，加一段刻意写成通用腔的对照，由另一 agent 判断归属。文件还记录了第一轮评审读取本地 skill 后作废的情况。
- `audit_style.py` 按预设区间检查表层指标；江南模式出现“道”系对白动词会被判为失败。

### 我们的判断

公开样本、失败记录和修订原因值得参考。但五段样本的归属判定主要支持风格可辨识性，不能证明同一篇小说经过修改后更好；95/100是项目评分卡的结果，不是通用创作质量分数。

统计与生成规则之间存在跳跃：笔记承认语料中有少量“笑道”，代码却将任何此类表达判为失败。比喻检测只统计部分标记，也不等于测量全部比喻。对我们的原创写作，这些指标适合作为复查线索，不宜成为配额。

覆盖说明也有待澄清：入口写《龙族1—4》，采样笔记中出现“龙族4—5”的标题；仅凭公开文件不能确认该处实际包含哪些版本。

来源：[江南模块](https://github.com/zuoyou12/longzu.skillls/blob/3f05bad7b6284c087f449d624fd6360f406e73f8/jiangnan-writer/SKILL.md)、[融合单文件版](https://github.com/zuoyou12/longzu.skillls/blob/3f05bad7b6284c087f449d624fd6360f406e73f8/standalone/style-writer-standalone.md)、[采样与统计笔记](https://github.com/zuoyou12/longzu.skillls/blob/3f05bad7b6284c087f449d624fd6360f406e73f8/style-writer/references/corpus-notes-jiangnan.md)、[评分卡与样本](https://github.com/zuoyou12/longzu.skillls/blob/3f05bad7b6284c087f449d624fd6360f406e73f8/FIDELITY.md)、[审计代码](https://github.com/zuoyou12/longzu.skillls/blob/3f05bad7b6284c087f449d624fd6360f406e73f8/style-writer/scripts/audit_style.py)。

## 3. cyberk1895/jiang-nan-skill

### 文件内容

- 主入口要求以作者身份、第一人称回应；用途包含创作诊断、人生选择与角色扮演。
- 研究目录涉及作品、访谈、表达、外部评价、决策、时间线及读者社区。
- `11-local-corpus-analysis.md` 明确说明原始GBK语料存在读取限制，该份分析主要依赖已有研究文档和 skill 的交叉比较，部分引文需转换编码后再核查。

### 我们的判断

可用于发现值得继续查找的访谈、文论和创作手记，但不应把其研究归纳直接当成我们已经核对过的原文。

上述读取限制针对该份分析，不能据此推断整个项目没有阅读原文；同样，也不能把该文件算作一次独立的全文复核。作者心理与创作原因的解释应保留为推断。其角色扮演目标与我们辅助用户原创小说的目标不同。

来源：[入口](https://github.com/cyberk1895/jiang-nan-skill/blob/d70c0ad03f4bd13dd1c5b77c82da832d80df0a15/SKILL.md)、[访谈线索](https://github.com/cyberk1895/jiang-nan-skill/blob/d70c0ad03f4bd13dd1c5b77c82da832d80df0a15/references/research/02-conversations.md)、[本地语料分析及方法说明](https://github.com/cyberk1895/jiang-nan-skill/blob/d70c0ad03f4bd13dd1c5b77c82da832d80df0a15/references/research/11-local-corpus-analysis.md)。

## 4. Carl24-star/jiang-nan-perspective

### 文件内容

- 主要提供文学创作、人物、IP商业化和创作者困境的分析视角，包含六个心智模型和八条启发式。
- 模型按观点、来源、应用和局限组织，访谈研究文件提供具体出处链接。
- 分析入口优先寻找衰小孩、孤独、求而不得与名场面；部分启发式将这些偏好进一步写成普遍判断。

### 我们的判断

观点附带适用条件和局限的组织方式可参考；具体材料仍需追溯原始来源。

这种带有强烈预设的视角可用于提出另一种解释，不宜统领原创写作。否则容易要求不同作品具备相同的主角类型、痛感内核或开篇方式，也可能把对作品的解释扩大成对真实创作者的因果判断。

来源：[入口、模型与启发式](https://github.com/Carl24-star/jiang-nan-perspective/blob/13fca1709b8a91072d1c4bb3de79052462fb23a7/SKILL.md)、[访谈资料与来源分级](https://github.com/Carl24-star/jiang-nan-perspective/blob/13fca1709b8a91072d1c4bb3de79052462fb23a7/references/research/02-conversations.md)。

## 与我们当前工作的关系

`jiangnan-fiction-craft` 0.1.0已有按问题选择章节、局部修改步骤、场景锚点和失效条件，并非只有阅读摘要。当前主要缺口是其他作品的直接阅读证据、长篇连续性管理及实际样稿验证。

本次只将外部调研存档。继续按[现有更新方式](update.md)积累自己的阅读与分析；《龙族》《天之炽》仍未纳入。外部项目的分析不能替代我们阅读这些书。

以后确有需要时，可回到本文考虑题材分流、连续性记录或同稿比较。尚未决定采用任何外部方案，也不将这些建议列为本轮实施任务。
