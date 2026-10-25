# jiangnan-fiction-craft

以江南小说的精读分析支持原创中文小说的构思、场景写作和修改。当前版本 **0.19.0**：保留已有分析，补充一段战役的多线切换与汇合回读。

已纳入《此间的少年》及后记、《龙族》六册、《九州·缥缈录》六册及《天之炽》两册，共189份章节分析、原89例细读、S1–S5五组句段分析、一条卷内关系线和[一段战役多线回读](references/techniques/multi-line-piaomiao-03.md)。逐卷范围、版本限制与来源见[书目索引](references/books/index.md)。

## 从哪里开始

| 用途 | 入口 |
|---|---|
| 让代理按当前任务使用本skill | [SKILL.md](SKILL.md) |
| 找现稿的问题、成文后回看 | [cheatsheet.md](cheatsheet.md) |
| 选择写法和适用条件 | [patterns.md](patterns.md) |
| 直接按语言、句段、描写、人物或情节查找 | [SKILL中的专题入口](SKILL.md#按需读取) |
| 按书查章节和证据 | [书目索引](references/books/index.md) |
| 理解术语 | [glossary.md](glossary.md) |
| 继续合入新书、核对来源或查看更新记录 | [来源与维护](references/maintenance/update.md) |

例如：

> 使用 jiangnan-fiction-craft 评审这章小说。先找影响阅读最大的一至三个问题，再给局部修改稿；保留人物设定、既定视角和事实边界。

阅读材料按问题加载，不需要每次通读全部书目，也不把分析表或检查清单写进小说。

## 目录

```text
SKILL.md                  任务、交付方式、核心判断与专题入口
cheatsheet.md             按现稿问题查找，成文后回看
patterns.md               九组方法、适用条件与反例入口
glossary.md               术语
chapters/                 189份章节分析；原文件名和编号保留
references/
  techniques/             语言、句段、描写、人物、情节、跨章与跨书分析
  books/                  书目总索引、逐卷索引及逐卷局部细读
  maintenance/            来源规则、更新记录与其他项目调研
sources/                  15份来源清单及《龙族》逐册状态
scripts/check_skill.py    无第三方依赖的结构检查
```

`SKILL.md`给出使用方式；`cheatsheet.md`集中具体问题；`patterns.md`比较方法；书目页负责定位原有分析。逐卷细读留在各书入口下，不把同一片段重复提炼成新的通用规则。

## 安装与使用边界

将整个仓库目录作为一个skill使用，保留上述相对路径。目录内的`SKILL.md`是入口；本版本不会自动安装到其他位置。

仓库包含分析、必要短引、来源指纹与覆盖记录，不包含小说全文、电子书、逐段reader或本机转换工作目录。原文锚点对应记录中的本地文字版本，不是纸书页码；版本未与指定纸本逐字校勘。

方法属于编辑归纳，不是作者自述理论，也不认证作者独有风格。已有少量构思和改稿自评对照，结果有得有失，尚不能证明稳定改善或独立因果效果。跨章与多线研究目前有一条卷内关系线和一段战役，未补成整卷主次线篇幅安排、跨卷总伏笔表或完整人物生涯研究。漫画方法也尚未经过作品研究与验证。

## 维护检查

在仓库根目录运行：

```sh
python3 scripts/check_skill.py
```

检查相对链接与章节锚点、书目可达性、来源定位边界、分析编号与清单对应，以及打包范围。检查不需要本地小说全文，也不能代替回读原文或实际写作比较。文件格式通过不表示文学效果通过。

继续阅读新书或补充方法时，沿用[来源与维护](references/maintenance/update.md)中的证据约束，保留已有分析。文本提取使用[book-to-skill](https://github.com/virgiliojr94/book-to-skill)；其他项目调研保留在[独立备忘](references/maintenance/related-skills.md)。
