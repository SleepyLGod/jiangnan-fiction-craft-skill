# 安装验证范围

2026-10-28 在 macOS 26.5、arm64、Codex CLI 0.164.0-alpha.11.1 上验证项目内安装；入口与用法见 [README](../../README.md#安装与验证codex)。这是安装与发现检查，不是模型写作测试。

## 实际做过的检查

- 从改名后的公开仓库按 v0.19.3 标签克隆到独立项目的 `.agents/skills/jiangnan-fiction-craft`，未使用 GitHub 登录凭证下载。
- 使用本机内置 skill-installer，从同一公开标签下载完整目录到另一独立项目；两份安装的 252 个发布文件逐一核对 SHA-256，全部一致。安装器的临时清理改为保留文件，未改其下载、校验和复制逻辑。
- 分别启动 Codex app-server，完成初始化后调用 `skills/list`。两次均返回本项目的 `SKILL.md` 实际路径、`scope: repo`、`enabled: true`，目标 skill 无解析错误；不是只按名称猜测发现成功。
- 在公开克隆中运行结构检查和五项既有回归测试，通过。来源清单与章节文件保持完整。

安装位置和发现方法分别依据 [Codex skills 说明](https://learn.chatgpt.com/docs/build-skills)与 [app-server 的 skills/list](https://learn.chatgpt.com/docs/app-server#skills)。本机临时路径、完整宿主日志不进入发布包。

## 能说明什么，不能说明什么

可以确认这套目录布局能下载、保留配套文件，并被上述版本 Codex 识别为可用的项目 skill。发布候选还会运行相同结构检查，标签推送后再从公开地址安装核对；最终状态以对应 Release 中的验证记录为准。

没有调用 `thread/start` 或 `turn/start`，没有模型生成和 token 用量测评；没有验证模型实际读了哪些材料、是否执行所有入口提醒，也没有手动操作桌面 skill 选择器。README 的首次调用问题供使用者自查，本轮未将它当作模型回答测试执行。其他宿主、其他系统和全局安装不在本次验证范围。

[完整编辑示例](usage-example.md)由AI 编写，只展示查例和改稿取舍，不补充上述运行验证，也不是独立效果实验。
