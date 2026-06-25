---
tags: [langsmith, concept, deep-agents]
created: 2026-06-25
updated: 2026-06-25
sources: [langsmith-deep-agents]
related: [concepts/mcp, concepts/sandboxes, concepts/fleet]
---

# Managed Deep Agents — Hosted Runtime cho Deep Agents

**Managed Deep Agents** (private beta) là hosted runtime cho deep agents — long-running agents có durable execution, sandboxed code execution, và MCP tool integration.

## Workflow

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
├── agent.json        # Config: name, model, backend
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

## Backend Types

| Type | Mô Tả | Khi Nào Dùng |
|------|-------|-------------|
| `state` | Không sandbox, đơn giản | Agent chỉ chat, không cần code |
| `sandbox` scope `thread` | Mỗi thread sandbox riêng | Code execution, phân lập |
| `sandbox` scope `agent` | Chung sandbox cho cả agent | Share files/state giữa các thread |

## SDKs & CLI

### Python SDK
```python
from managed_deepagents import Client
client = Client()  # reads LANGSMITH_API_KEY

# Deploy
client.agents.deploy("path/to/project")

# Run
for chunk in client.runs.stream(thread_id, agent_id, input=input):
    print(chunk)
```

### CLI
```bash
deepagents init [name]           # Scaffold
deepagents deploy                # Deploy
deepagents agents list           # List agents
deepagents agents delete <id>    # Delete
deepagents mcp-servers add ...   # Add MCP tools
```

## MCP Tools Integration
```bash
# Register MCP server
deepagents mcp-servers add \
  --url https://api.github.com/mcp \
  --name github-tools

# List available tools
deepagents mcp-servers tools github-tools

# Connect with OAuth
deepagents mcp-servers add \
  --url https://example.com/mcp \
  --name my-tools \
  --auth-type oauth --connect
```

## Trang Liên Quan
- [MCP](mcp.md) — MCP protocol
- [Sandboxes](sandboxes.md) — Isolated environments
- [Fleet](fleet.md) — No-code agent platform
