# AI Agent & LLM 基础知识笔记专栏

用**大白话 + 架构图 + 可交互模拟器**，从零拆解 LLM 底层原理与现代 AI Agent 架构。

> 💡 **GitHub Pages 在线交互实验室**：`https://zhangdingsong.github.io/ai-agent-notes/`

---

## 📚 笔记目录（`notes/`）

### 基础篇：Token、API 与产业观察
1. [第一篇：Token、上下文窗口、上限归属与速率限流](notes/第一篇：Token、上下文窗口、上限归属与速率限流.md)
2. [一文看懂大模型速率 - Rate Limit, Speed, Price 是怎么影响你账单的](notes/一文看懂大模型速率%20-%20Rate%20Limit,%20Speed,%20Price%20是怎么影响你账单的.md)
3. [API 与产品的区别](notes/API%20与产品的区别.md)
4. [第二篇：🧠 AI 进阶通识：从开源权重、Meta Muse 到 API 与限流机制](notes/第二篇：🧠%20AI%20进阶通识：从开源权重、Meta%20Muse%20到%20API%20与限流机制.md)
5. [第二篇独立进阶笔记](notes/第二篇独立进阶笔记.md)
6. [AI 时代，软件行业定规则的人为什么换成了华人面孔？](notes/AI%20时代，软件行业定规则的人为什么换成了华人面孔？.md)

### Agent 篇：核心引擎与扩展能力
7. [LLM Fundamental - LLM Inference](notes/LLM%20Fundamental%20-%20LLM%20Inference.md) · [🎮 交互图解](demos/llm-inference.html)
8. [LLM fundamental - ReAct Loop：AI Agent 的底层心脏](notes/LLM%20fundamental%20-%20ReAct%20Loop：AI%20Agent%20的底层心脏.md) · [🎮 交互模拟器](demos/react-loop.html)
9. [LLM fundamental - 让 AI Agent 真正变强的三件套：RAG、MCP 与 Subagent](notes/LLM%20fundamental%20-%20让%20AI%20Agent%20真正变强的三件套：RAG、MCP%20与%20Subagent.md) · [🎮 交互实验室](demos/agent-tools.html)

---

## 🎮 交互式实验室（`demos/`）

| 实验室 | 说明 | 在线地址 |
|---|---|---|
| **LLM Inference** | Prefill / Decode / KV Cache 交互指南 | [打开](demos/llm-inference.html) |
| **ReAct Loop** | Thought → Action → Observation 步进模拟器 | [打开](demos/react-loop.html) |
| **RAG · MCP · Subagent** | Agent 三大扩展能力痛点对比实验室 | [打开](demos/agent-tools.html) |

---

## 💻 实战代码（`code/`）

- [mini_react_agent.py](code/mini_react_agent.py)

---

## 🖼️ 视觉总览（`assets/`）

![ReAct Loop 交互演示](assets/react-loop-demo.gif)
