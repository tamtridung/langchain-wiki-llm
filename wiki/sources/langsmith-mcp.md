---
tags: [langsmith, source, mcp]
created: 2026-06-25
updated: 2026-06-25
sources: [raw/langchain_docs/langsmith/langsmith-remote-mcp.md, raw/langchain_docs/langsmith/server-mcp.md, raw/langchain_docs/langsmith/managed-deep-agents-mcp.md, raw/langchain_docs/langsmith/fleet/mcp-framework.md, raw/langchain_docs/langsmith/fleet/remote-mcp-servers.md]
related: [concepts/mcp, concepts/tools]
---

# Nguồn: MCP (Model Context Protocol) trong LangSmith

## Tóm Tắt

5 files về MCP trong LangSmith ecosystem — từ remote MCP server đến Agent Server MCP endpoint và Fleet MCP framework.

## Điểm Then Chốt

### MCP là gì?
**Model Context Protocol (MCP)** là open protocol chuẩn hoá để mô tả tools và data sources dưới dạng model-agnostic, cho phép LLMs khám phá và sử dụng chúng qua structured API.

### 4 Cách MCP trong LangSmith

#### 1. LangSmith Remote MCP
- MCP server được LangSmith tự host, không cần triển khai riêng
- Exposes: conversation history, prompts, runs, datasets, experiments, billing
- Auth: OAuth 2.1 (interactive clients) hoặc API key (programmatic clients)
- Cloud endpoints: GCP US, GCP EU, GCP APAC, AWS US
- Self-hosted: `https://<host>/api/mcp`

#### 2. Agent Server MCP Endpoint
- LangGraph agents deployed qua Agent Server được expose thành MCP tools
- Endpoint: `/mcp` trên Agent Server URL
- Dùng Streamable HTTP transport
- **Stateless** — mỗi request là độc lập
- Yêu cầu: `langgraph-api >= 0.2.3`

#### 3. Managed Deep Agents MCP
- Kết nối MCP tools cho Managed Deep Agents
- Workspace-level resources; LangSmith quản lý per-user OAuth
- CLI: `deepagents mcp-servers add/remove/tools`

#### 4. Fleet MCP Framework
- LangSmith Tool Server — standalone MCP framework build/deploy custom tools
- `@tool` decorator, built-in Agent Auth OAuth
- Dùng khi cần custom toolkits ngoài Fleet

## Code Mẫu

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

```python
# Agent Server MCP client
from langchain_mcp_adapters.tools import load_mcp_tools
tools = await load_mcp_tools(session)
agent = create_react_agent(model, tools)
```

## Trang Liên Quan
- [MCP](../concepts/mcp.md)
- [Tools](../concepts/tools.md)
- [Deployment](../concepts/deployment.md)
