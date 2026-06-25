---
tags: [langchain, langsmith, concept, mcp]
created: 2026-06-25
updated: 2026-06-25
sources: [langsmith-mcp]
related: [concepts/tools, concepts/deployment]
---

# MCP (Model Context Protocol) trong LangChain/LangSmith

**Model Context Protocol (MCP)** là open protocol cho phép LLMs khám phá và sử dụng tools qua structured API. LangSmith cung cấp 4 cách tích hợp MCP.

## MCP trong LangSmith

```
                ┌──────────────────────────────────┐
                │      MCP-Compliant Clients        │
                │  (Claude Code, Cursor, AI SDK...) │
                └──────────────┬───────────────────┘
                               │
          ┌────────────────────┼────────────────────┐
          ▼                    ▼                    ▼
   ┌─────────────┐    ┌───────────────┐    ┌──────────────┐
   │ LangSmith   │    │ Agent Server  │    │ Fleet / Deep │
   │ Remote MCP  │    │ MCP Endpoint  │    │ Agents  MCP  │
   │ (Cloud)     │    │ (/mcp)        │    │ (Workspace)  │
   └─────────────┘    └───────────────┘    └──────────────┘
```

### 1. LangSmith Remote MCP
MCP server được LangSmith tự host. Exposes LangSmith tools (prompts, datasets, experiments, traces) cho MCP clients.

```json
// Claude Code .mcp.json
{
  "mcpServers": {
    "langsmith": {
      "type": "http",
      "url": "https://api.smith.langchain.com/mcp"
    }
  }
}
```

- **Auth**: OAuth 2.1 (interactive) hoặc API key (programmatic)
- **Endpoints**: GCP US, GCP EU, GCP APAC, AWS US
- **Available tools**: Conversation history, prompts, runs, datasets, experiments, billing

### 2. Agent Server MCP Endpoint
LangGraph agents deployed qua Agent Server được expose thành MCP tools.

```python
from langchain_mcp_adapters.tools import load_mcp_tools
tools = await load_mcp_tools(session)
agent = create_react_agent(model, tools)
```

- Endpoint: `/mcp` trên Agent Server URL
- Streamable HTTP transport
- **Stateless** — mỗi request độc lập
- Yêu cầu `langgraph-api >= 0.2.3`

### 3. Fleet MCP Framework (Tool Server)
Standalone framework để build/deploy custom tools với built-in auth.

```python
from langsmith_tool_server import tool

@tool
def hello(name: str) -> str:
    """Greet someone by name."""
    return f"Hello, {name}!"
```

### 4. Managed Deep Agents MCP
Kết nối MCP tools với Deep Agents qua CLI:

```bash
deepagents mcp-servers add --url https://example.com/mcp --name my-tools
```

## Authentication

| Phương thức | Dùng cho | Cách hoạt động |
|---|---|---|
| **OAuth 2.1** | Interactive clients (Claude Code, Cursor) | Dynamic Client Registration |
| **API key** | Programmatic clients | `X-Api-Key` header |
| **Custom headers** | Self-hosted MCP | Configurable per server |

## Trang Liên Quan
- [Tools](tools.md) — Tools & function calling
- [Fleet](fleet.md) — Fleet platform
- [Managed Deep Agents](managed-deep-agents.md) — Deep Agents
- [Deployment](deployment.md) — Agent Server
