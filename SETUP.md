# 新电脑 / 新 Agent 快速恢复指南

换到一台新的 Mac，或者切换成其他 AI 编程助手（Antigravity、Codex、Claude Code、Gemini CLI、Muse Code、Workbuddy 等）时，按下面步骤操作，**30 秒即可恢复全部记忆与自动同步能力**。

---

## 一、在新电脑上恢复环境（只需 2 步）

### 1. 克隆仓库并安装本地同步钩子
```bash
git clone https://github.com/zhangdingsong/ai-agent-notes.git
cd ai-agent-notes
chmod +x scripts/setup.sh
./scripts/setup.sh
```
运行 `./scripts/setup.sh` 后，会自动把 `.git/hooks/post-commit` 链接到 `scripts/post-commit.py`。此后每次 `git commit`，`notes/*.md` 都会自动转换并同步到本机的 iCloud Obsidian 目录：
`~/Library/Mobile Documents/iCloud~md~obsidian/Documents/VaultDS/AI基础知识/`

*(注：前提是这台 Mac 已登录同一个 Apple ID 并开启了 iCloud Drive 与 Obsidian 同步。)*

### 2. 用任意 Agent 打开项目目录
在 **Antigravity / Codex / Claude Code / Cursor / Gemini CLI / Muse Code / Workbuddy** 中打开 `ai-agent-notes` 文件夹即可：
- Antigravity 会自动加载 `.agents/rules/sync-obsidian.md` + `AGENTS.md`
- Codex / Cursor / Muse 等会自动加载根目录 `AGENTS.md`
- Gemini 系列会自动加载 `GEMINI.md`（软链接至 `AGENTS.md`）
- Claude 系列 / Workbuddy 会自动加载 `CLAUDE.md`（软链接至 `AGENTS.md`）

---

## 二、如果使用“不挂载本地文件夹”的纯聊天 App（如网页版 / 独立桌面聊天）

对于无法直接读取项目文件夹的纯聊天应用，只需在该应用的 **Custom Instructions（自定义指令 / Saved Info）** 中添加以下一句即可：

> 当我讨论 `ai-agent-notes` 项目或让你帮我整理 AI 学习笔记时，如果能访问本地目录，请先读取 `~/Projects/ai-agent-notes/AGENTS.md` 并严格遵守其中的规范；如果是纯对话环境，草稿先让我确认定稿后再输出最终 Markdown。

---

## 三、日常协作口令（推荐）

- **开始聊新主题时**：`我们先在 drafts/ 里讨论 <主题>，先不要进 notes/`
- **确认成品收录时**：`定稿了，帮我收录进正式目录，更新目录并 commit`
- **定期清理草稿时**：`帮我清理掉已经定稿的 drafts/ 子目录`
