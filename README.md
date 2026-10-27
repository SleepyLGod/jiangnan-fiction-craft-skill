# jiangnan-fiction-craft

以江南小说精读证据为依据的中文小说写作参考库，支持查例、比较写法与适用条件，以及按需构思、续写和修改。当前版本 **0.19.3**：补齐文字与脚本的分路径许可、第三方材料声明及相应检查，保留已有分析和用法。

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
  maintenance/            来源规则、更新记录与其他项目调研
sources/                  15份来源清单及《龙族》逐册状态
scripts/check_skill.py    无第三方依赖的结构检查
LICENSE                   文字与脚本的许可范围
NOTICE                    小说引文与第三方材料声明
LICENSES/                 CC BY 4.0、MIT 完整条款
```

`SKILL.md`给出使用方式；`cheatsheet.md`集中具体问题；`patterns.md`比较方法；书目页负责定位原有分析。逐卷细读留在各书入口下，不把同一片段重复提炼成新的通用规则。

## 安装与使用边界

将整个仓库目录作为一个skill使用，保留上述相对路径。目录内的`SKILL.md`是入口；本版本不会自动安装到其他位置。

仓库包含分析、必要短引、来源指纹与覆盖记录，不包含小说全文、电子书、逐段reader或本机转换工作目录。原文锚点对应记录中的本地文字版本，不是纸书页码；版本未与指定纸本逐字校勘。

方法属于编辑归纳，不是作者自述理论，也不认证作者独有风格。现有本地样稿与Luna小样本比较有局部帮助，也有交付遗漏和评阅分歧，尚不能证明稳定改善或独立因果效果；最新入口提醒尚未完成修订后的使用验证。跨章与多线研究目前有一条卷内关系线和一段战役，未补成整卷主次线篇幅安排、跨卷总伏笔表或完整人物生涯研究。漫画方法也尚未经过作品研究与验证。

## 许可

本项目按路径分别授权，具体范围见 [LICENSE](LICENSE)：

| 范围 | 许可 |
|---|---|
| 贡献者有权许可的文字、精读分析、方法说明与资料编排 | [CC BY 4.0 完整条款](LICENSES/CC-BY-4.0.txt) |
| `scripts/` 下的脚本和回归测试 | [MIT 完整条款](LICENSES/MIT.txt) |
| 小说引文和其他第三方受保护材料 | 不在上述授权范围内，见 [NOTICE](NOTICE) |

文字可按 CC BY 4.0 使用、修改和商用，需适当署名、链接许可并注明修改；脚本按 MIT 保留版权和许可声明。独立分析的许可不等于原著授权。本项目不声称获得原作作者、出版方或所调研项目的官方背书。

## 维护检查

在仓库根目录运行：

```sh
python3 scripts/check_skill.py
python3 -B -m unittest discover -s scripts -p test_check_skill.py
```

检查相对链接与章节锚点、书目可达性、来源定位边界、分析编号与清单对应、打包范围及许可文件是否齐全。许可文件检查不认证每处第三方引用的合法性，也不代替回读原文或实际写作比较。文件格式通过不表示文学效果通过。

文件范围遵循当前`.gitignore`中的文件名通配和目录排除，保留未提交的新分析；检查不依赖Git。若新增当前匹配器不支持的忽略语法，脚本会明确报错。发布文档不能链接到被排除的本地材料。

继续阅读新书或补充方法时，沿用[来源与维护](references/maintenance/update.md)中的证据约束，保留已有分析。文本提取使用[book-to-skill](https://github.com/virgiliojr94/book-to-skill)；其他项目调研保留在[独立备忘](references/maintenance/related-skills.md)。
