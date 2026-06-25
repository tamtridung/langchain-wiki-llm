---
tags: [langsmith, source, engine]
created: 2026-06-25
updated: 2026-06-25
sources: [raw/langchain_docs/langsmith/engine.md, raw/langchain_docs/langsmith/engine-overview.md, raw/langchain_docs/langsmith/engine-link.md, raw/langchain_docs/langsmith/engine-webhooks.md]
related: [concepts/engine, concepts/evaluation, concepts/monitoring]
---

# Nguồn: LangSmith Engine

## Tóm Tắt

4 files về LangSmith Engine — "AI agent cho agent engineering".

## Điểm Then Chốt

### Là gì?
**LangSmith Engine** là AI agent phát hiện và sửa lỗi tự động từ production traces. Tạo closed loop: phát hiện lỗi → chẩn đoán nguyên nhân → đề xuất fix → deploy evaluator → auto-reopen nếu tái phát.

### Workflow
1. Phát hiện recurring failure từ traces
2. Chẩn đoán root cause
3. Đề xuất fix (sửa prompt, model, evaluator)
4. Deploy evaluator để monitor
5. Auto-reopen nếu issue chưa được fix

### Engine Link
Kết nối Engine với issue tracker (GitHub Issues, Linear, Jira, v.v.) để tự động tạo/track issues.

### Webhooks
Event-driven triggers khi Engine phát hiện vấn đề mới hoặc có insight quan trọng.

## Trang Liên Quan
- [Engine](../concepts/engine.md)
- [Evaluation](../concepts/evaluation.md)
- [Monitoring](../concepts/monitoring.md)
