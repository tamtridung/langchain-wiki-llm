---
tags: [langsmith, source, deep-agents]
created: 2026-06-25
updated: 2026-06-25
sources: [raw/langchain_docs/langsmith/managed-deep-agents-overview.md, raw/langchain_docs/langsmith/managed-deep-agents-quickstart.md, raw/langchain_docs/langsmith/managed-deep-agents-deploy.md, raw/langchain_docs/langsmith/managed-deep-agents-sdk.md, raw/langchain_docs/langsmith/managed-deep-agents-cli.md, raw/langchain_docs/langsmith/managed-deep-agents-mcp.md]
related: [concepts/managed-deep-agents, concepts/mcp, concepts/sandboxes]
---

# Nguồn: Managed Deep Agents

## Tóm Tắt

6 files về Managed Deep Agents — hosted runtime cho deep agents (private beta).

## Điểm Then Chốt

### Là gì?
**Managed Deep Agents** là hosted runtime (private beta, US region) cho phép tạo, chạy và vận hành deep agents trên LangSmith mà không cần tự setup infrastructure.

### Workflow
1. `deepagents init research-assistant` — Scaffold project
2. Cấu hình `agent.json` (model, backend, name)
3. `deepagents deploy` — Deploy lên LangSmith
4. Run via SDK: `client.runs.create(...)`

### Project Structure
```
my-agent/
├── agent.json        # Config: name, model, backend
├── AGENTS.md         # Agent instructions
├── tools.json        # MCP-backed tools
├── skills/           # Skills directory
├── subagents/        # Sub-agents directory
└── .gitignore
```

### Backend Types
- `state` — Không sandbox, lưu state đơn giản
- `sandbox` scope `"thread"` — Mỗi thread có sandbox riêng
- `sandbox` scope `"agent"` — Chung sandbox cho cả agent

### SDKs
- Python: `managed-deepagents` (≥ 3.10)
- TypeScript: `@langchain/managed-deepagents`
- React: `@langchain/react`

### CLI
```bash
deepagents init [name]          # Scaffold project
deepagents deploy               # Deploy project
deepagents agents list          # List agents
deepagents mcp-servers add      # Add MCP tools
```

## Trang Liên Quan
- [Managed Deep Agents](../concepts/managed-deep-agents.md)
- [MCP](../concepts/mcp.md)
- [Sandboxes](../concepts/sandboxes.md)
