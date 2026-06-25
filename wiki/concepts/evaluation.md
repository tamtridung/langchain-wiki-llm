---
tags: [langsmith, concept, evaluation]
created: 2026-06-25
updated: 2026-06-25
---

# Evaluation — Đánh Giá Chất Lượng Ứng Dụng LLM

**Evaluation** trong LangSmith cho phép bạn đánh giá chất lượng output của chain/agent một cách có hệ thống, dùng datasets làm ground truth.

## Evaluation Approaches

| Approach | Khi Nào Dùng |
|----------|-------------|
| **Offline evals** | Pre-deployment: benchmark, regression test |
| **Online evals** | Production: monitor quality real-time |
| **LLM-as-judge** | Không có ground truth, dùng LLM để chấm |
| **Code evals** | Có metric định lượng (accuracy, precision) |
| **Human evals** | Cần domain expert đánh giá |

## Quick Start

```python
from langsmith import Client, evaluate
from langsmith.evaluation import evaluate as ls_evaluate

client = Client()

# 1. Tạo dataset
dataset = client.create_dataset(
    "qa-dataset",
    description="Q&A test set"
)
client.create_examples(dataset_id=dataset.id, inputs=[
    {"question": "What is LangChain?"},
    {"question": "What is RAG?"},
])

# 2. Định nghĩa evaluator
def correctness(inputs, outputs):
    if outputs["answer"] and len(outputs["answer"]) > 10:
        return {"key": "has_answer", "score": 1}
    return {"key": "has_answer", "score": 0}

# 3. Run evaluation
experiment = ls_evaluate(
    lambda inputs: {"answer": my_chain.invoke(inputs["question"])},
    data="qa-dataset",
    evaluators=[correctness],
)

# 4. View results
print(experiment.results)
```

## Evaluators

### 1. LLM-as-Judge

```python
from langsmith.evaluation import StringEvaluator

def answer_relevance(outputs, reference):
    """Use LLM to judge answer relevance."""
    response = judge_model.invoke(
        f"Question: {reference['question']}\n"
        f"Answer: {outputs['answer']}\n"
        f"Is this answer relevant? (0-10): "
    )
    score = int(response.content.strip())
    return {"key": "relevance", "score": score / 10}
```

### 2. Code Evaluators

```python
def exact_match(inputs, outputs):
    """Exact match scoring."""
    expected = inputs["expected"]
    actual = outputs["answer"]
    return {
        "key": "exact_match",
        "score": 1 if expected == actual else 0
    }

def contains_required(inputs, outputs):
    """Check if answer contains required keywords."""
    required = inputs.get("required_keywords", [])
    answer = outputs["answer"].lower()
    score = sum(1 for kw in required if kw.lower() in answer) / len(required)
    return {"key": "keyword_coverage", "score": score}
```

### 3. Composite Evaluators

```python
from langsmith.evaluation import evaluate

def composite_eval(run, examples):
    """Combine multiple metrics."""
    scores = {
        "relevance": relevance_eval(run, examples),
        "faithfulness": faithfulness_eval(run, examples),
        "completeness": completeness_eval(run, examples),
    }
    scores["overall"] = sum(scores.values()) / len(scores)
    return scores
```

## Offline vs Online Evaluation

### Offline (Batch)

```python
# Chạy test với dataset
experiment = evaluate(
    my_chain,
    data="qa-dataset",
    evaluators=[exact_match, llm_as_judge],
    experiment_prefix="gpt4-vs-claude",
    max_concurrency=5,
)
```

### Online (Production)

```python
# Gán feedback real-time từ users
from langsmith import Client

client = Client()

# User click thumbs up/down
client.create_feedback(
    run_id=trace_id,
    key="user_rating",
    score=1,  # 1 = positive, 0 = negative
    comment="Great answer!"
)

# Hoặc auto-label trong production
@traceable
def my_endpoint(input):
    response = chain.invoke(input)
    # Auto-evaluate
    if len(response) < 10:
        client.create_feedback(
            run_id=..., key="too_short", score=0
        )
    return response
```

## Agent Evaluation (3 Scopes)

| Scope | Mô Tả | Đo Lường |
|-------|-------|----------|
| **Final Response** | Black box: input → output | Correctness, relevance |
| **Single Step** | Tool call correctness | Tool selection, params, timing |
| **Trajectory** | Path of tool calls | Was the reasoning path optimal? |

```python
# Evaluate compiled LangGraph agent
from langgraph.prebuilt import create_react_agent

agent = create_react_agent(model, tools)

results = evaluate(
    agent,
    data="agent-test-set",
    evaluators=[correctness, tool_usage_eval],
)
```

## RAG Evaluation

| Type | Cần Ground Truth? | Ví Dụ |
|------|-------------------|-------|
| **Answer Correctness** | ✅ Yes | So sánh answer với expected |
| **Faithfulness** | ❌ No | Answer có đúng với context? |
| **Relevance** | ❌ No | Answer có trả lời câu hỏi? |
| **Context Precision** | ❌ No | Retrieved docs có relevant? |

## Online Evaluators (Production)

Online evaluators chạy trên production traces real-time:

```python
# Viết trong LangSmith UI
# Restriction: không network access
# Libraries: numpy, pandas, jsonschema, scipy, sklearn

def online_eval(inputs, outputs) -> dict:
    # Chỉ dùng thư viện được whitelist
    return {"key": "quality", "score": 0.95}
```

⚠️ **Online evaluator restrictions**:
- Không network access (no API calls)
- Thư viện giới hạn (5 whitelisted packages)
- Scored traces auto-upgrade lên extended data retention
- Evaluators là workspace-level resources

## Composite Evaluators

```python
# langsmith>=0.4.29
def composite_summary(inputs, outputs) -> dict:
    """Combine multiple scores với custom aggregation."""
    scores = []
    for eval_fn in [relevance, faithfulness, completeness]:
        result = eval_fn(inputs, outputs)
        scores.append(result["score"])
    
    return {
        "key": "overall_quality",
        "score": sum(scores) / len(scores),
        "individual": scores
    }
```

## Evaluator Types So Sánh

| Type | Speed | Accuracy | Effort | Use Case |
|------|-------|----------|--------|----------|
| **Code** | ⚡ Nhanh | 📊 Objective | Thấp | Unit tests, CI/CD |
| **LLM-as-Judge** | 🐢 Chậm | 🧠 Good | Trung bình | Quality scoring |
| **Composite** | 🐢 Chậm | 🎯 High | Cao | Production monitoring |
| **Human** | 🐌 Chậm | 👑 Best | Rất cao | Final validation |
| **Pairwise** | 🐢 Chậm | 🎯 High | Cao | A/B comparison |

## Spend Tracking

LangSmith tự động track chi phí evaluators:

```python
# Xem trong UI: per-evaluator USD spend columns
# Breakdown: Input tokens, Output tokens, Cache reads, Reasoning tokens

# Custom model pricing
@traceable(run_type="llm", metadata={
    "ls_provider": "my_provider",
    "ls_model_name": "my_model"
})
def my_evaluator(inputs):
    ...
```

## Run Evaluation với REST API

Không cần SDK — dùng raw HTTP requests:

```python
import requests

# 1. Fetch examples
# 2. Tạo experiment
# 3. POST runs với reference_example_id và session_id
requests.post(f"{api_url}/runs", json={
    "name": "MyEvaluator",
    "run_type": "llm",
    "inputs": example["inputs"],
    "outputs": {"output": prediction},
    "session_id": experiment_id,
    "reference_example_id": example["id"],
})
# 4. Close experiment
```

## Experiment Comparison

```python
# So sánh kết quả giữa các experiments
experiment_v1 = evaluate(chain_v1, data="qa-dataset", evaluators=[...])
experiment_v2 = evaluate(chain_v2, data="qa-dataset", evaluators=[...])

# So sánh trong UI hoặc code
for eval_result in experiment_v1.comparisons(experiment_v2):
    print(f"{eval_result.key}: v1={eval_result.v1_score} vs v2={eval_result.v2_score}")
```

## Best Practices

1. **Dataset > 50 examples** — Đủ để có statistical significance
2. **Đa dạng evaluators** — Kết hợp LLM-judge + code metrics + human
3. **Test trên nhiều models** — So sánh GPT-4 vs Claude vs Gemini
4. **CI/CD integration** — Auto-run evals trên mỗi PR
5. **Monitor regression** — So sánh với experiment trước đó
6. **Human annotation** — Dùng annotation queues cho qualitative feedback

## Trang Liên Quan

- [Datasets](datasets.md) — Tạo và quản lý datasets
- [Tracing](tracing.md) — Ghi lại traces cho evaluation
- [LangSmith Overview](langsmith-overview.md) — Tổng quan
