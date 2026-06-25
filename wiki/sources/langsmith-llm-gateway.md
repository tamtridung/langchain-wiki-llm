---
tags: [langsmith, source, llm-gateway]
created: 2026-06-25
updated: 2026-06-25
sources: [raw/langchain_docs/langsmith/llm-gateway.md, raw/langchain_docs/langsmith/llm-gateway-custom-providers.md, raw/langchain_docs/langsmith/llm-gateway-redaction.md, raw/langchain_docs/langsmith/llm-gateway-spend-policies.md]
related: [concepts/llm-gateway, concepts/administration]
---

# Nguồn: LangSmith LLM Gateway

## Tóm Tắt

4 files về LLM Gateway — proxy, redaction, và spend policies cho LLM calls.

## Điểm Then Chốt

### Là gì?
LLM Gateway là unified proxy cho tất cả LLM calls trong organization — cung cấp auth, redaction, routing, và spend control.

### Custom Providers
Thêm model providers không được LangSmith support sẵn:
- OpenAI-compatible API endpoints
- Anthropic-compatible API endpoints
- Custom auth headers

### Redaction
Tự động redact PII/sensitive data khỏi LLM requests/replies trước khi lưu traces:
- Pattern-based (regex, email, SSN, API keys)
- LLM-powered detection
- Works with any provider

### Spend Policies
- Budget limits per user/team/project
- Rate limiting per model/provider
- Alerts khi vượt threshold
- Monthly/quarterly reset

## Trang Liên Quan
- [LLM Gateway](../concepts/llm-gateway.md)
- [Administration](../concepts/administration.md)
- [Monitoring](../concepts/monitoring.md)
