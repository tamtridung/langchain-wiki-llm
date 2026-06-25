---
tags: [langsmith, concept, engine]
created: 2026-06-25
updated: 2026-06-25
sources: [langsmith-engine]
related: [concepts/evaluation, concepts/monitoring]
---

# Engine — AI Agent Cho Agent Engineering

**LangSmith Engine** là AI agent phát hiện và sửa lỗi tự động từ production traces. Nó tạo closed loop: phát hiện → chẩn đoán → đề xuất fix → deploy evaluator → monitor.

## Closed Loop Workflow

```
Production Traces
       │
       ▼
┌──────────────────────┐
│ 1. Phát hiện lỗi     │  ← Recurring failure patterns
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ 2. Chẩn đoán root    │  ← Phân tích traces, tìm nguyên nhân
│    cause             │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ 3. Đề xuất fix       │  ← Sửa prompt, model, evaluator
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ 4. Deploy evaluator  │  ← Monitor cho issue tương tự
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ 5. Auto-reopen       │  ← Nếu issue tái phát
└──────────────────────┘
```

## Key Features

### Engine Link
Kết nối Engine với issue tracker:
- GitHub Issues
- Linear
- Jira
- Tự động tạo/track issues từ phát hiện của Engine

### Webhooks
Event-driven triggers:
- "New issue detected"
- "Fix proposed"
- "Issue resolved"
- "Issue re-opened"

### Self-hosted
Engine có thể chạy trên self-hosted LangSmith instance.

## Best Practices

1. **Start với 1-2 metrics** — Không bật hết cùng lúc
2. **Kết nối issue tracker** — Dùng Engine Link để auto-track
3. **Review đề xuất trước khi deploy** — Engine đề xuất, người duyệt
4. **Monitor auto-reopen rate** — Nếu cao → cần fix sâu hơn

## Trang Liên Quan
- [Evaluation](evaluation.md) — Evaluators
- [Monitoring](monitoring.md) — Alerts & dashboards
- [Administration](administration.md) — Webhook config
