---
trigger: always_on
description: 强制加载项目根目录 AGENTS.md 中的跨 Agent 与 Obsidian 同步规范
---

# Antigravity 工作区规则

请严格遵守项目根目录 [AGENTS.md](../../AGENTS.md) 中的全部规范，尤其是：
1. 中间草稿与实验文件只放 `drafts/YYYY-MM-DD-<主题>/`（已被 `.gitignore` 忽略），未经用户明确确认“定稿/收录”，禁止写入 `notes/`、`demos/`、`assets/`；
2. `notes/*.md` 中不写 `<iframe>`，图片用 `../assets/<filename>`，交互页用 `https://zhangdingsong.github.io/ai-agent-notes/demos/<name>.html`；
3. 定稿收录后同步更新 `_sidebar.md` 与 `README.md`。
