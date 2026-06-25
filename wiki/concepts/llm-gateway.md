---
tags: [langsmith, concept, llm-gateway]
created: 2026-06-25
updated: 2026-06-25
sources: [langsmith-llm-gateway]
related: [concepts/administration, concepts/monitoring]
---

# LLM Gateway — Unified Proxy Cho LLM Calls

**LLM Gateway** là unified proxy cho tất cả LLM calls trong organization — cung cấp auth, redaction, routing, và spend control tập trung.

## Architecture

```
App / Agent
    │
    ▼
┌──────────────────────┐
│    LLM Gateway       │
│ • Authentication     │
│ • Redaction (PII)    │
│ • Route to provider  │
│ • Spend tracking     │
│ • Rate limiting      │
└──────┬───────────────┘
       │
       ▼
OpenAI / Anthropic / Google / Custom
```

## Key Features

### Custom Providers
```python
# Thêm model provider không được support sẵn
# OpenAI-compatible endpoints
# Anthropic-compatible endpoints
# Custom auth headers
```

### Redaction
Tự động redact PII/sensitive data khỏi LLM requests/replies:
- Pattern-based: email, SSN, API keys, credit cards
- LLM-powered detection cho unstructured data
- Works với mọi provider qua gateway

### Spend Policies
```python
# Budget limits per user/team/project
# Rate limiting per model/provider
# Alerts khi vượt threshold
# Monthly/quarterly reset
```

## Use Cases
- **Centralized auth** — Một API key cho tất cả providers
- **Compliance** — Redact PII trước khi lưu traces
- **Cost control** — Budget alerts, rate limiting
- **Migration** — Route traffic giữa providers không đổi code

## Best Practices
1. **Enable redaction cho production** — Tránh lộ PII trong traces
2. **Set spend policies sớm** — Tránh cost spike
3. **Monitor gateway metrics** — Latency, error rate, cost

## Trang Liên Quan
- [Administration](administration.md) — Auth & compliance
- [Monitoring](monitoring.md) — Cost tracking
- [Tracing](tracing.md) — Trace redaction
