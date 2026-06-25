---
tags: [langsmith, source, evaluation]
created: 2026-06-25
updated: 2026-06-25
sources: [raw/langchain_docs/langsmith/evaluation.md, raw/langchain_docs/langsmith/evaluation-concepts.md, raw/langchain_docs/langsmith/evaluation-approaches.md, raw/langchain_docs/langsmith/evaluation-types.md, raw/langchain_docs/langsmith/evaluators.md, raw/langchain_docs/langsmith/llm-as-judge.md, raw/langchain_docs/langsmith/code-evaluator-sdk.md, raw/langchain_docs/langsmith/composite-evaluators-sdk.md, raw/langchain_docs/langsmith/online-evaluations-code.md, raw/langchain_docs/langsmith/evaluate-llm-application.md, raw/langchain_docs/langsmith/evaluate-rag-tutorial.md, raw/langchain_docs/langsmith/evaluate-graph.md, raw/langchain_docs/langsmith/evaluate-complex-agent.md]
related: [concepts/evaluation, concepts/datasets, concepts/tracing]
---

# Nguồn: LangSmith Evaluation

## Tóm Tắt

13 files về evaluation trong LangSmith — từ khái niệm đến implementation chi tiết.

## Điểm Then Chốt

### Evaluation Approaches
- **Offline**: Test trên curated datasets trước khi deploy
- **Online**: Monitor production traces real-time

### Evaluator Types
1. **LLM-as-Judge** — Dùng LLM để chấm điểm (prompt-based scoring)
2. **Code Evaluators** — Python/JS functions, chạy trong sandbox, **không có network access**
3. **Composite Evaluators** — Kết hợp nhiều scores, custom aggregation (`langsmith>=0.4.29`)
4. **Human** — Annotation queues, rubric feedback
5. **Pairwise** — So sánh A vs B

### Agent Evaluation (3 scopes)
- **Final response** — Black box: input → output
- **Single step** — Đánh giá tool call correctness
- **Trajectory** — Path của tool calls có đúng không

### RAG Evaluation
- Reference-required: answer correctness so với ground truth
- Reference-free: self-consistency, hallucinations, relevance

### Online Evaluators
- Được viết inline trong LangSmith UI
- Thư viện giới hạn: numpy, pandas, jsonschema, scipy, sklearn
- ⚠️ **Không network access**
- Auto-upgrade scored traces lên extended data retention

### Evaluation Types
- **Benchmarking** — So sánh models/prompts
- **Unit tests** — CI-friendly, rule-based
- **Regression tests** — Diff view (red/green)
- **Backtesting** — Historical production data
- **Pairwise** — Relative quality

### Graph Evaluation
- Dùng `evaluate()` với compiled graph
- Hỗ trợ đánh giá intermediate steps/nodes

## Code Mẫu

```python
# Graph evaluation
from langgraph.graph import StateGraph
workflow = StateGraph(State)
# ... build graph ...
app = workflow.compile(checkpointer=memory)

results = evaluate(app, data="dataset_name", evaluators=[...])

# Online evaluator - code
def correct(outputs: dict, reference_outputs: dict) -> bool:
    return outputs["answer"] == reference_outputs["answer"]
```

## Trang Liên Quan
- [Evaluation](../concepts/evaluation.md)
- [Datasets](../concepts/datasets.md)
- [RAG](../concepts/rag.md)
