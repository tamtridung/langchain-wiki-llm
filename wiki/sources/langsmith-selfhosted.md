---
tags: [langsmith, source, deployment, selfhosted]
created: 2026-06-25
updated: 2026-06-25
sources: [raw/langchain_docs/langsmith/self-hosted.md, raw/langchain_docs/langsmith/self-host-scale.md, raw/langchain_docs/langsmith/self-host-ttl.md, raw/langchain_docs/langsmith/self-hosted-changelog.md, raw/langchain_docs/langsmith/configuration-cloud.md]
related: [concepts/deployment]
---

# Nguồn: LangSmith Self-hosted

## Tóm Tắt

5 files về self-hosted deployment của LangSmith platform.

## Điểm Then Chốt

### Architecture Components
- **Frontend UI** + **Backend API** + **Platform Backend** + **Playground** + **Queue** + **ACE Backend**
- **ClickHouse** — Traces & feedback
- **PostgreSQL** — Operational data
- **Redis** — Queuing & caching
- **Blob storage** — Optional (artifacts)

### Requirements
- **Enterprise license**
- **Kubernetes** (Helm charts provided)
- **KEDA** recommended cho auto-scaling

### Scaling (Resource Table)
| Load Pattern | Platform Backend | Ingest Queue | Backend | ClickHouse |
|-------------|-----------------|--------------|---------|------------|
| Low/Low | 3 replicas | 4 replicas | 6 replicas | Single node |
| Med/Med | 8 replicas | 10 replicas | 20 replicas | 2 nodes |
| High/High (1000 traces/s) | 20 replicas | 24 replicas | 50 replicas | 3 replicas |

### TTL & Data Retention
- `longlived` (default 400 ngày) và `shortlived` (default 14 ngày)
- ClickHouse TTL cleanup: `ALTER TABLE DELETE` — expensive, chạy weekends
- Configurable via Helm

## Trang Liên Quan
- [Deployment](../concepts/deployment.md)
- [LangSmith Overview](../concepts/langsmith-overview.md)
