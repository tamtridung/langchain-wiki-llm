---
tags: [langsmith, source, fleet, agents]
created: 2026-06-25
updated: 2026-06-25
sources: [raw/langchain_docs/langsmith/fleet/*]
related: [concepts/fleet, concepts/multi-agent, concepts/deployment]
---

# Nguồn: LangSmith Fleet

## Tóm Tắt

~25 files về Fleet — nền tảng no-code của LangSmith để tạo, quản lý và deploy AI agents.

## Điểm Then Chốt

### Fleet là gì?
Fleet (formerly Agent Builder) là **no-code platform** trong LangSmith ecosystem cho phép tạo AI agents mà không cần viết code. Chạy trên Deep Agents runtime.

### Architecture
```
User → [Chat UI / Slack / Teams / Schedule / API]
                  ↓
         ┌─────────────────┐
         │   Fleet Agent   │  ← Instructions, Skills, Sub-agents, Memory
         ├─────────────────┤
         │ • Built-in Tools│  (Gmail, Calendar, Slack, GitHub...)
         │ • Remote MCP    │  (External tools via HTTPS)
         │ • Virtual PC    │  (Code execution, file management)
         └────────┬────────┘
                  ↓
         ┌─────────────────┐
         │   LangSmith     │  (Tracing, Eval, Observability)
         └─────────────────┘
```

### Key Features
- **Model-agnostic** — Bất kỳ LLM nào (OpenAI/Anthropic-compatible)
- **Channels** — Deploy lên Slack, Teams, Gmail, Web
- **Schedules** — Cron-based recurring runs (UTC)
- **Human-in-the-Loop** — Centralized approvals inbox
- **Self-updating agents** — Agents tự thêm/xoá tools, update instructions
- **Skills** — Reusable capability bundles (`SKILL.md`)
- **Sub-agents** — Chia tác vụ lớn thành helper agents
- **Virtual computer** — Isolated environment cho code execution
- **Code export** — Export thành MIT-licensed Python project

### Agent Identity
- **Fixed credentials ("Claws")** — Shared service account (cho channels/schedules)
- **User credentials ("Assistants")** — Per-user OAuth (cho personal tools)

### Security Model (3 layers)
1. Agent-level: Clone / Run / Edit permissions
2. Credential-level: Fixed vs Per-user
3. Tool-level: RBAC + ABAC + Workspace policy (Enterprise)

### Fleet vs Alternatives
| Tiêu Chí | Fleet | Claude Cowork | MS Copilot |
|----------|-------|---------------|------------|
| Model-agnostic | ✅ | ❌ Claude-only | ❌ |
| Self-hosted | ✅ Beta | ❌ | ❌ |
| Export to code | ✅ MIT | ❌ | ❌ |
| LangSmith tracing | ✅ Native | ❌ | ❌ |
| Self-updating | ✅ | ❌ | ❌ |

## Trang Liên Quan
- [Fleet](../concepts/fleet.md)
- [Multi-Agent](../concepts/multi-agent.md)
- [Deployment](../concepts/deployment.md)
- [Administration](../concepts/administration.md)
