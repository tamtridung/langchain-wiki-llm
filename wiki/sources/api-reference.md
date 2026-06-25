---
tags: [langsmith, source, api]
created: 2026-06-25
updated: 2026-06-25
sources: [raw/langchain_docs/api-reference/*]
related: [concepts/deployment, concepts/langsmith-overview]
---

# Nguồn: LangSmith API Reference

## Tóm Tắt

5 API reference groups từ `raw/langchain_docs/api-reference/`.

## Agent Connections v2

3 endpoints quản lý kết nối agent:
- `POST /agent-connections` — Tạo connection mới
- `GET /agent-connections` — List connections
- `DELETE /agent-connections/:id` — Xoá connection

## Auth Service v2

18 endpoints cho OAuth 2.0 authentication:
- OAuth provider CRUD (create, read, update, delete)
- OAuth token management (list, revoke, delete)
- MCP OAuth provider support
- Slack token management
- Callback handlers (setup, callback GET/POST)

## Deployments v2

9 endpoints quản lý deployment:
- CRUD deployments
- Revision management (get, list, redeploy)
- Batch delete

## Integrations v1

4 endpoints cho GitHub integration:
- List GitHub/Forge integrations
- List repositories từ integrations

## Listeners v2

5 endpoints cho event listeners:
- CRUD listeners
- List listeners với filtering

## Trang Liên Quan
- [Deployment](../concepts/deployment.md)
- [LangSmith Overview](../concepts/langsmith-overview.md)
