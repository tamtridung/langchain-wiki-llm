---
tags: [langsmith, source, data]
created: 2026-06-25
updated: 2026-06-25
sources: [raw/langchain_docs/langsmith/data-export.md, raw/langchain_docs/langsmith/data-purging-compliance.md, raw/langchain_docs/langsmith/data-storage-and-privacy.md, raw/langchain_docs/langsmith/data-export-destinations.md, raw/langchain_docs/langsmith/big-query-bulk-export.md]
related: [concepts/tracing, concepts/langsmith-overview]
---

# Nguồn: LangSmith Data Management

## Tóm Tắt

5 files về data export, purging, compliance, privacy trong LangSmith.

## Điểm Then Chốt

### Bulk Export (Plus/Enterprise)
- Export traces to S3-compatible buckets in **Parquet** format
- Tạo destination → export job (project + date range) → monitor
- Hỗ trợ filters, scheduled exports, field filtering
- 72-hour runtime timeout

### Data Retention
- Base: **14 ngày**
- Extended: up to **400 ngày** (default)
- Enterprise: custom period (30–400 ngày)
- Configurable at workspace/project level

### Privacy
- CLI telemetry: opt-out via `LANGGRAPH_CLI_NO_ANALYTICS=1`
- In-memory dev server: lưu local `.langgraph_api` directory
- Docker server: PostgreSQL + Redis
- **Studio runs in-browser** — không data gửi đến LangSmith
- Tracing disable: `LANGSMITH_TRACING=false`
- Checkpoint encryption: `LANGGRAPH_AES_KEY`

### Export Destinations
- AWS S3, GCS (S3-compatible API + HMAC keys), MinIO
- Minimal IAM: `s3:PutObject`
- Credentials stored encrypted

## Trang Liên Quan
- [Tracing](../concepts/tracing.md)
- [Deployment](../concepts/deployment.md)
- [LangSmith Overview](../concepts/langsmith-overview.md)
