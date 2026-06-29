---
tags: [langchain, deep-agents, concept]
created: 2026-06-29
updated: 2026-06-29
sources: [deep-agents-sdk]
related: [concepts/mcp, concepts/deep-agents-overview, concepts/deep-agents-customization]
---

# Deep Agents — Agent Client Protocol (ACP)

**Agent Client Protocol (ACP)** là giao thức tiêu chuẩn cho communication giữa coding agents và code editors/IDEs. Deep Agents có thể expose qua ACP để tích hợp với Zed, JetBrains, VS Code, Neovim.

> ACP dành cho agent-editor integrations. Để agent gọi tools từ external servers, dùng [MCP](mcp.md).

## Quickstart

```bash
pip install deepagents-acp
```

```python
import asyncio
from acp import run_agent
from deepagents import create_deep_agent
from langgraph.checkpoint.memory import MemorySaver
from deepagents_acp.server import AgentServerACP

async def main():
    agent = create_deep_agent(
        model="google_genai:gemini-3.5-flash",
        system_prompt="You are a helpful coding assistant",
        checkpointer=MemorySaver(),
    )
    server = AgentServerACP(agent)
    await run_agent(server)

asyncio.run(main())
```

## Clients

| IDE | Setup |
|-----|-------|
| **Zed** | Register ACP server command trong `settings.json` |
| **JetBrains** | Native ACP support |
| **VS Code** | Via `vscode-acp` extension |
| **Neovim** | Via ACP-compatible plugins |

### Zed Example

```json
{
  "agent_servers": {
    "DeepAgents": {
      "type": "custom",
      "command": "/path/to/deepagents/libs/acp/run_demo_agent.sh"
    }
  }
}
```

### Toad (Local Dev)

```bash
uv tool install -U batrachian-toad
toad acp "python path/to/your_server.py" .
```

## Trang Liên Quan

- [MCP](mcp.md) — Model Context Protocol
- [Deep Agents Overview](deep-agents-overview.md) — Tổng quan Deep Agents
- [Deep Agents Customization](deep-agents-customization.md) — Tạo agent với tools
