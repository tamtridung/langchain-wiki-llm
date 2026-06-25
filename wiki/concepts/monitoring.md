---
tags: [langsmith, concept, monitoring, observability]
created: 2026-06-25
updated: 2026-06-25
sources: [langsmith-production]
related: [concepts/tracing, concepts/langsmith-overview]
---

# Monitoring — Giám Sát Production

**Monitoring** trong LangSmith cung cấp khả năng quan sát và cảnh báo cho ứng dụng LLM ở production — từ dashboards real-time đến alerts và cost tracking.

## Alerts

Threshold-based alerting cho LLM applications:

| Metric | Mô Tả |
|--------|-------|
| **Run Count** | Số lượng runs trong window |
| **Cost** | Tổng chi phí tokens |
| **Errors** | Số lỗi xảy ra |
| **Feedback Score** | Điểm feedback trung bình |
| **Latency** | Thời gian xử lý |

### Routing
- PagerDuty, Dynatrace, Slack, MS Teams, Email
- Webhook-based — tích hợp với bất kỳ system nào

### Configuration
```python
# Alert conditions (configured in UI)
# - Project-scoped
# - Aggregation windows: 5 min hoặc 15 min
# - Filter by: Status, Run Type, Tag, Error strings
```

## Dashboards

### Prebuilt Dashboards
Tự động generate per project:
- Traces overview
- LLM calls analytics
- Cost & Token usage
- Tool usage patterns
- Run types distribution
- Feedback scores

### Custom Dashboards
```python
# Fully custom charts
# - Group by tags/metadata
# - Multiple data series
# - Line/Bar chart types
```

⚠️ **Important**: Tags/metadata không tự propagate từ parent → child runs. Phải set explicitly trên cả hai nếu muốn group charts.

## Cost Tracking

### Automatic
```python
# Tự động cho LangChain, @traceable, SDK wrappers
# Breakdown: Input/Output/Other tokens
# Subtypes: cache reads, reasoning tokens
```

### Manual (Non-LangChain Models)
```python
@traceable(run_type="llm", metadata={
    "ls_provider": "my_provider",
    "ls_model_name": "my_model"
})
def my_chat_model(messages: list):
    response = openai.chat.completions.create(...)
    return response
```

## Insights

AI-powered trace analysis:

```python
from langsmith import Client
client = Client()

report = client.generate_insights(
    chat_histories=chat_histories,
    name="Customer Support Topics",
    instructions="What are the main topics?",
    openai_api_key=os.environ["OPENAI_API_KEY"],
)
```

- Phát hiện patterns, behaviors, failure modes
- Dùng **sampled** subset of traces
- Report generation ~30 phút
- Cost: ~$1-2 / 1000 threads
- Yêu cầu Plus/Enterprise plan

## Best Practices

1. **Set alerts sớm** — Cost spike, error rate, latency degradation
2. **Metadata propagation** — Set tags/metadata trên cả root và child runs
3. **Cost tracking cho mọi model** — Kể cả non-LangChain LLM calls
4. **Prebuilt dashboards first** — Rồi mới custom khi cần
5. **Regular insights** — Chạy insights reports định kỳ để phát hiện drift

## Trang Liên Quan
- [Tracing](tracing.md) — Observability cơ bản
- [LangSmith Overview](langsmith-overview.md) — Tổng quan
- [Evaluation](evaluation.md) — Đánh giá chất lượng
