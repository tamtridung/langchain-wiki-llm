---
tags: [langsmith, source, monitoring]
created: 2026-06-25
updated: 2026-06-25
sources: [raw/langchain_docs/langsmith/alerts.md, raw/langchain_docs/langsmith/dashboards.md, raw/langchain_docs/langsmith/cost-tracking.md, raw/langchain_docs/langsmith/insights.md]
related: [concepts/tracing]
---

# Nguồn: LangSmith Production Monitoring

## Tóm Tắt

4 files về production monitoring trong LangSmith: alerts, dashboards, cost tracking, insights.

## Điểm Then Chốt

### Alerts
- Threshold-based: Run Count, Cost, Errors, Feedback Score, Latency
- Routing: PagerDuty, Dynatrace, Slack, MS Teams, email (webhook)
- Project-scoped, aggregation windows 5 hoặc 15 phút
- Yêu cầu Helm chart 0.10.3+ cho self-hosted

### Dashboards
- **Prebuilt** — Auto-generated per project (traces, LLM calls, cost/tokens, tools, feedback)
- **Custom** — Configurable charts, group-by (tags/metadata), multiple series, line/bar
- ⚠️ Tags/metadata không propagate từ parent → child runs

### Cost Tracking
- **Automatic** — Token counts + model pricing (LangChain, `@traceable`, SDK wrappers)
- **Manual** — Custom costs trên bất kỳ run type nào
- Breakdown: Input/Output/Other tokens, subtype (cache reads, reasoning tokens)
- Non-LangChain LLM: cần set `ls_provider`, `ls_model_name` trong metadata

### Insights
- AI-powered trace analysis
- Detect usage patterns, agent behaviors, failure modes
- **Sampled** subset of traces, report takes ~30 phút
- Cost: ~$1-2 / 1000 threads với OpenAI
- `client.generate_insights()` cho external chat histories

## Code Mẫu

```python
# Cost tracking custom model
@traceable(run_type="llm", metadata={
    "ls_provider": "my_provider",
    "ls_model_name": "my_model"
})
def my_chat(messages: list):
    ...

# Insights SDK
report = client.generate_insights(
    chat_histories=chat_histories,
    name="Customer Support Topics",
    openai_api_key=os.environ["OPENAI_API_KEY"],
)
```

## Trang Liên Quan
- [Tracing](../concepts/tracing.md)
- [LangSmith Overview](../concepts/langsmith-overview.md)
