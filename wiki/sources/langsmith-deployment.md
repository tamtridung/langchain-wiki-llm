---
tags: [langsmith, langgraph, source, deployment]
created: 2026-06-25
updated: 2026-06-25
sources: [raw/langchain_docs/langsmith/deployment.md, raw/langchain_docs/langsmith/deploy-to-cloud.md, raw/langchain_docs/langsmith/deployment-quickstart.md, raw/langchain_docs/langsmith/deploy-with-control-plane.md, raw/langchain_docs/langsmith/deploy-to-self-hosted-overview.md]
related: [concepts/deployment, concepts/langsmith-overview]
---

# Nguồn: LangSmith Deployment

## Tóm Tắt

5 files về deployment trong LangSmith — từ cloud đến self-hosted.

## Điểm Then Chốt

### Deployable Products
- **Deep Agents** (managed)
- **LangGraph** (CLI + templates)
- **Google ADK**
- **Other frameworks** (Claude Agent SDK, CrewAI, AutoGen) via `deployments-wrap-sdk`

### Deployment Topologies (3)
1. **Cloud** — Fully managed trên AWS/GCP
2. **Self-hosted** — Full platform trong K8s của bạn
3. **Standalone server** — Docker + Postgres/Redis, không control plane

### Cloud Deployment Methods
- **LangSmith UI** — GitHub OAuth + auto-deploy on push
- **`langgraph deploy` CLI** — Docker Build + push

### Deployment Types
- **Dev** — Minimal resources
- **Production** — Up to 500 req/s, HA storage with backups

### Agent Server Architecture
- **Assistants** (config) → **Threads** (state) → **Runs** (workloads)
- Runtime: Single host (dev), Split API/queue (scalable), Distributed (high concurrency)
- Queue workers = execution engine; API servers chỉ handle requests
- Tự động inject checkpointer và memory store
- **Không config checkpointer/memory store trong graph code** khi deploy

### CLI Commands
```bash
langgraph deploy                    # dev deployment
langgraph deploy --name my-agent --deployment-type prod
langgraph deploy list               # list deployments
langgraph deploy logs               # tail logs
langgraph deploy delete <ID>        # remove
```

### Cron Jobs & Background Runs
- Cron: schedule agent runs với cron expressions (UTC)
- Background runs: `client.runs.create()` — non-blocking

## Trang Liên Quan
- [Deployment](../concepts/deployment.md)
- [LangGraph Overview](../concepts/langgraph-overview.md)
- [LangSmith Overview](../concepts/langsmith-overview.md)
