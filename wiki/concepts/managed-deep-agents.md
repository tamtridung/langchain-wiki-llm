---
tags: [langsmith, langchain, concept, deep-agents]
created: 2026-06-25
updated: 2026-06-29
sources: [deep-agents-sdk, langsmith-deep-agents]
related: [concepts/mcp, concepts/sandboxes, concepts/fleet, concepts/deep-agents-overview, concepts/deep-agents-production]
---

# Managed Deep Agents — Hosted Runtime cho Deep Agents

**Managed Deep Agents** (private beta) là hosted runtime trên LangSmith để tạo, chạy, và vận hành deep agents. Nó kết hợp **Deep Agents harness** với managed infrastructure: durable runs, LangSmith sandboxes, thread state, MCP tools, file trees, traces, và agent revisions.

> Hiện tại private beta, chỉ available trên LangSmith Cloud US region. [Join waitlist](https://www.langchain.com/langsmith-managed-deep-agents-waitlist).

## Workflow

```
1. Tạo/edit local Managed Deep Agents project
2. Giữ default backend hoặc opt-in LangSmith sandbox
3. Connect MCP tools khi cần
4. Deploy project lên Managed Deep Agents
5. Run agent với Python/TypeScript SDK
6. Inspect traces, files, tool calls, runtime state trong LangSmith
```

```bash
# 1. Scaffold project
deepagents init research-assistant

# 2. Deploy lên LangSmith
deepagents deploy

# 3. Run via SDK
python -c "
from managed_deepagents import Client
client = Client()
for chunk in client.runs.stream(thread_id, agent_id, input=input):
    print(chunk)
"
```

## Project Structure

```
my-agent/
├── agent.json        # Config: name, model, backend, MCP tools
├── AGENTS.md         # Agent instructions (system prompt)
├── tools.json        # MCP-backed tools config
├── skills/           # Reusable skills
├── subagents/        # Helper sub-agents
└── .gitignore
```

### agent.json
```json
{
  "name": "research-assistant",
  "description": "A research assistant agent.",
  "model": "openai:gpt-5.5",
  "backend": { "type": "sandbox", "scope": "thread" }
}
```

Model identifiers dùng format `{provider}:{model_id}` (vd: `openai:gpt-5.5`). Runtime resolve models với `init_chat_model`.

## Created Resources

Khi tạo Managed Deep Agent, LangSmith provisions:
1. **Managed Deep Agent resource**
2. **LangSmith tracing project** riêng cho agent
3. **Context Hub agent repo** — lưu managed file tree (instructions, skills, subagents, tools)

Không tạo LangSmith Deployment.

## Sandbox Backends

Managed Deep Agents projects dùng `state` backend mặc định:

```json
{ "backend": { "type": "state" } }
```

| Backend | Scope | Mô Tả |
|---------|-------|-------|
| `state` | — | Không sandbox-specific behavior |
| `sandbox` | `thread` | Sandbox resources per thread (phân lập) |
| `sandbox` | `agent` | Sandbox chung cho cả agent |

## SDKs & CLI

### Python SDK
```python
from managed_deepagents import Client
client = Client()  # reads LANGSMITH_API_KEY

# Deploy
client.agents.deploy("path/to/project")

# Run — streaming API
for chunk in client.runs.stream(thread_id, agent_id, input=input):
    print(chunk)
```

### CLI
```bash
deepagents init [name]           # Scaffold project
deepagents deploy                # Deploy (update)
deepagents agents list           # List agents
deepagents agents delete <id>    # Delete agent
deepagents mcp-servers add ...   # Register MCP server
deepagents mcp-servers tools ... # List MCP tools
```

### REST API
Routes: `/v1/deepagents/*` (private beta, có thể thay đổi).

## MCP Tools Integration

### Static Header MCP
```bash
deepagents mcp-servers add \
  --url https://api.github.com/mcp \
  --name github-tools
```

### OAuth MCP
```bash
deepagents mcp-servers add \
  --url https://example.com/mcp \
  --name my-tools \
  --auth-type oauth --connect
```

## Limits (Private Beta)

| Item | Limit |
|------|-------|
| Workspace free plan | 1 agent tối đa |
| Paid plans | Unlimited agents |
| Thread retention | No limit (trong beta) |
| Rate limits | None enforced |
| Regions | US only |
| Self-hosted/Hybrid | Not supported |

### Delete Agents
`DELETE /v1/deepagents/agents/{agent_id}` không cascade đến threads. Threads từ agent đã xóa vẫn queryable nhưng không start được run mới.

## Use Cases

- Tạo và quản lý deep agents từ local project files
- Long-running agents không cần tự setup server
- Isolated LangSmith sandbox resources per thread/agent
- Stream runs + persist thread state
- Managed file tree cho instructions, skills, tools
- Workspace-level MCP servers (bao gồm OAuth)
- Inspect traces, files, tool calls, runtime state trong LangSmith

Dùng **LangSmith Deployment** thay thế khi cần: custom application code, custom routes, advanced authentication, full Agent Server APIs, maximum scalability.

## Trang Liên Quan
- [Deep Agents Overview](deep-agents-overview.md) — Deep Agents SDK
- [Deep Agents Production](deep-agents-production.md) — Production guide
- [MCP](mcp.md) — MCP protocol
- [Sandboxes](sandboxes.md) — Isolated environments
- [Fleet](fleet.md) — No-code agent platform
