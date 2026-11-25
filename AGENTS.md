# AI Agent Notes 工作区规范（跨 Agent 通用）

> 本文件是仓库的唯一规范源（Single Source of Truth）。`GEMINI.md`、`CLAUDE.md` 为其软链接，`.agents/rules/sync-obsidian.md` 亦指向本规范。

## 1. 草稿区 vs 正式发布区（严防中间文件污染）

- **讨论与试错阶段**：
  - 会话过程中生成的临时 `.md`、实验性 `.html`、试画的配图或 GIF，一律放在 `drafts/`（已被 `.gitignore` 忽略）或 Agent 自带的会话临时目录中。
  - **禁止**未经用户确认直接写入 `notes/`、`demos/`、`assets/`。
- **`drafts/` 内部整理规范**：
  - 禁止在 `drafts/` 根目录平铺文件，必须按 `drafts/YYYY-MM-DD-<主题>/` 建子目录归类存放。
  - 拆帧图、转换脚本等一次性过程垃圾放系统临时目录，不放进 `drafts/`。
  - 一旦主题定稿移入正式目录，同步清理或归档对应的 `drafts/` 子目录，不留双份。
- **定稿收录阶段**：
  - 只有当用户明确表示“定稿 / 收录进专栏 / 同步笔记”时，才将最终确认的成品移入正式目录（`notes/`、`demos/`、`assets/`）。
  - `demos/` 和 `assets/` 中只保留被正式笔记或 `README.md` 实际引用的有效素材。

## 2. 正式目录分工

- `notes/`：正式 Markdown 笔记（文件名即标题，无需强行在第一行手写 `# 标题`，GitHub Pages 的 Docsify 会自动补全）。
- `demos/`：独立、离线可运行的交互式 HTML Demo（使用简短小写英文文件名，如 `react-loop.html`）。
- `assets/`：正式配图与 GIF 动图。
- `code/`：配套实战代码。
- `scripts/`：跨设备本地自动化脚本（如 `post-commit.py` 与 `setup.sh`）。

## 3. 笔记书写规范（兼容 GitHub + GitHub Pages + Obsidian）

- **图片引用**：`notes/*.md` 中统一使用相对路径 `../assets/<filename>`。
- **交互 Demo 引用**：`notes/*.md` 中统一写完整 GitHub Pages 链接：
  `https://zhangdingsong.github.io/ai-agent-notes/demos/<name>.html`
- **禁止手写 `<iframe>`**：不要在 `notes/*.md` 中直接写 `<iframe>` 标签（GitHub 网页会将其渲染为纯文本）。GitHub Pages 的 `index.html` 会在网页端自动将 `demos/*.html` 链接转为内嵌交互框；本地 Obsidian 版则由 `post-commit` 钩子在同步时自动补全。
- **目录同步**：新增、重命名或删除 `notes/*.md` 后，同步更新 `_sidebar.md` 和 `README.md`。

## 4. 跨设备与 Obsidian 自动同步

- 本仓库通过 `scripts/post-commit.py` 实现本地单向投递：每次 `git commit` 后，自动将 `notes/*.md` 转换图片路径并补全 `<iframe>`，同步到本机的 `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/VaultDS/AI基础知识/`。
- 在新电脑克隆本仓库后，只需执行一次 `./scripts/setup.sh` 即可激活本地 Git Hook。
