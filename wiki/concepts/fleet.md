---
tags: [langsmith, concept, fleet, agents]
created: 2026-06-25
updated: 2026-06-25
sources: [langsmith-fleet]
related: [concepts/multi-agent, concepts/deployment, concepts/administration, concepts/mcp]
---

# Fleet — Nền Tảng Agent Không Code

**Fleet** là nền tảng no-code của LangSmith để tạo, quản lý và deploy AI agents. Chạy trên Deep Agents runtime, tích hợp sẵn LangSmith tracing và evaluation.

## Architecture

```
User ──┬── Chat UI (trong LangSmith)
       ├── Slack / Teams
       ├── Schedule (cron)
       └── API / SDK
            │
            ▼
     ┌──────────────┐
     │ Fleet Agent  │ ← Instructions, Skills, Sub-agents, Memory
     ├──────────────┤
     │ • Built-in   │ (Gmail, Calendar, Slack, GitHub, BigQuery...)
     │ • Remote MCP │ (External tools via HTTPS)  
     │ • Virtual PC │ (Code execution, file management)
     └──────┬───────┘
            ▼
     ┌──────────────┐
     │  LangSmith   │ (Tracing, Eval, Observability)
     └──────────────┘
```

## Key Concepts

### Agent Identity
- **Fixed credentials ("Claws")** — Shared service account. Dùng cho channels/schedules
- **User credentials ("Assistants")** — Per-user OAuth. Audit trail per-user

### Channels
Kênh deploy agent:
| Channel | Cách Hoạt Động |
|---------|---------------|
| **Slack** | Custom bot (tag-based + DMs) hoặc default bot (channel-wide) |
| **Teams** | Azure Bot via Bot Framework |
| **Gmail** | Trigger trên emails mới |
| **Web Chat** | Chat UI trong LangSmith |
| **Schedule** | Cron-based recurring runs |
| **API** | LangGraph SDK / REST API |

### Skills
Reusable capability bundles (dạng `SKILL.md`). Loaded vào long-term memory:
- **Private** — 1 agent
- **Shared** — Tất cả agents trong workspace, tự động sync khi update

### Security Model (3 layers)
1. **Agent-level**: Clone / Run / Edit permissions
2. **Credential-level**: Fixed vs Per-user
3. **Tool-level**: RBAC + ABAC + Workspace policy (Enterprise)

### Self-Updating Agents
Agents có thể tự thêm/xoá tools, update instructions tại runtime — không platform nào khác có.

## Fleet vs Alternatives

| Tiêu Chí | Fleet | Claude Cowork | MS Copilot |
|----------|-------|---------------|------------|
| Model-agnostic | ✅ Any LLM | ❌ Claude-only | ❌ |
| Self-hosted | ✅ Beta | ❌ | ❌ |
| Export to code | ✅ MIT-licensed | ❌ | ❌ |
| LangSmith tracing | ✅ Native | ❌ | ❌ |
| Self-updating | ✅ | ❌ | ❌ |

## Best Practices

1. **Bắt đầu từ template** — Daily calendar brief, Email assistant
2. **Dùng Fixed credentials cho team agents** — Slack bot, daily briefing
3. **Dùng User credentials cho personal agents** — Email assistant
4. **Set spend limits** — Per-agent, per-user, reset Monday
5. **Enable HIL** — Centralized approvals inbox cho sensitive actions

## Trang Liên Quan
- [MCP](mcp.md) — MCP protocol & tools
- [Multi-Agent](multi-agent.md) — Multi-agent patterns
- [Managed Deep Agents](managed-deep-agents.md) — Deep Agents runtime
- [Administration](administration.md) — Auth & RBAC
- [Deployment](deployment.md) — Self-hosted Fleet
