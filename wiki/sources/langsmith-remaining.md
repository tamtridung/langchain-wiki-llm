---
tags: [langsmith, source, remaining]
created: 2026-06-25
updated: 2026-06-25
sources: [raw/langchain_docs/langsmith/* — various remaining files]
related: [concepts/evaluation, concepts/tracing, concepts/deployment, concepts/chat-models, concepts/langsmith-overview]
---

# Nguồn: Các File Còn Lại (P4)

## Tóm Tắt

~30 files còn lại từ `raw/langchain_docs/langsmith/` chưa được nhóm vào các source page chính.

## Nhóm 1: OpenTelemetry

### OTEL Gateway Trace Redaction
- Redact sensitive data qua OTEL Gateway
- Dùng OTel Collector để filter/redact traces trước khi gửi đến LangSmith

### Evaluate with OpenTelemetry
- Dùng OTel để collect evaluation metrics
- Export traces từ non-LangChain apps qua OTel SDK

## Nhóm 2: Chat & Messages

### Chat Observability & Evaluation
- Chat-specific tracing: user messages, AI responses, tool calls
- Chat evaluation metrics: coherence, relevance, engagement

### Messages View
- Format và integration cho messages view trong LangSmith UI
- Multimodal content support (text, images, audio)
- Multiple messages patterns (one-to-many, many-to-one)

## Nhóm 3: CI/CD & Testing

### CI/CD Pipeline Example
```yaml
# GitHub Actions example
- name: Run evaluations
  run: |
    python -m pytest tests/ --eval-dataset qa-dataset
```
- Tích hợp evaluation vào CI/CD pipeline
- Auto-fail pipeline nếu quality không đạt threshold

### pytest Integration
```python
# pytest marker cho evaluations
@pytest.mark.langsmith
def test_chain_quality():
    results = evaluate(chain, data="test-set", evaluators=[...])
    assert results.avg_score > 0.8
```

### Multi-turn Simulation
- Tạo multi-turn conversations để test agent
- Simulate user behavior patterns

## Nhóm 4: Experiments & Analysis

### Experiment Analysis
- `analyze-an-experiment.md` — Phân tích kết quả experiment
- `compare-experiment-results.md` — So sánh experiment side-by-side
- `experiment-configuration.md` — Config experiment parameters
- `filter-experiments-ui.md` — Filter experiments trong UI
- `fetch-perf-metrics-experiment.md` — Lấy performance metrics
- `run-backtests-new-agent.md` — Backtest agent mới với historical data

## Nhóm 5: Setup & Integration

### Setup Guides
- `setup-pyproject.md` — Python pyproject.toml configuration
- `setup-app-requirements-txt.md` — Requirements.txt setup
- `setup-javascript.md` — JavaScript/TypeScript setup
- `get-started-integrations.md` — Integration quickstart
- `harbor-integrations.md` — Harbor container integration

### Config & Customization
- `configurable-headers.md` — Configurable HTTP headers cho tracing
- `configurable-logs.md` — Configurable logging levels
- `model-configurations.md` — Model config management
- `managing-model-configurations.md` — Managing model configs
- `playground-model-providers.md` — Thêm model providers vào Playground
- `custom-lifespan.md` — Custom lifespan hooks cho Agent Server
- `custom-middleware.md` — Custom middleware cho Agent Server

### Generative UI
- `generative-ui-react.md` — Build generative UI components với React
- Stream responses với React Server Components

## Nhóm 6: Platform & Production

### Platform Features
- `monorepo-support.md` — Monorepo structure support
- `serverless-environments.md` — Deploy lên serverless platforms
- `shared-responsibility-model.md` — LangSmith shared security model
- `govern.md` — Governance policies
- `graph-rebuild.md` — Rebuild LangGraph graphs
- `granular-usage.md` — Granular usage tracking
- `optimize-classifier.md` — Optimize LLM-as-judge classifiers
- `openevals.md` — OpenEvals library
- `quick-start-studio.md` — LangSmith Studio quickstart
- `observability-stack.md` — Full observability stack
- `reference.md` — Reference documentation
- `rules.md` — Rule-based evaluations
- `local-dev-testing.md` — Local development & testing
- `components.md` — LangSmith components overview
- `hybrid.md` — Hybrid deployment
- `hybrid-legacy.md` — Legacy hybrid deployment

## Nhóm 7: Agent Server Chi Tiết

- `agent-server-distributed-tracing.md` — Distributed tracing cho Agent Server
- `agent-server-scale.md` — Scaling Agent Server
- `agent-server-changelog.md` — Agent Server changelog

## Trang Liên Quan
- Tất cả concept pages hiện có
