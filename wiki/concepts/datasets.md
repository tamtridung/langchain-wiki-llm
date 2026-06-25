---
tags: [langsmith, concept, datasets, evaluation]
created: 2026-06-25
updated: 2026-06-25
---

# Datasets — Quản Lý Bộ Dữ Liệu Test

**Datasets** trong LangSmith là bộ sưu tập các cặp **input-output** (hoặc input-only) dùng để đánh giá chain/agent. Datasets là nền tảng của evaluation pipeline.

## Tạo Dataset

### Từ Code

```python
from langsmith import Client

client = Client()

# Tạo dataset
dataset = client.create_dataset(
    dataset_name="rag-test-set",
    description="Test set for RAG pipeline"
)

# Thêm examples
client.create_examples(
    dataset_id=dataset.id,
    inputs=[
        {"question": "What is LangChain?"},
        {"question": "Explain RAG architecture"},
        {"question": "How does LCEL work?"},
    ],
    outputs=[
        {"answer": "A framework for building LLM applications"},
        {"answer": "Retrieval-Augmented Generation combines retrieval with generation"},
        {"answer": "LCEL is a declarative way to chain components using | operator"},
    ],
    # Optional metadata per example
    metadata=[
        {"category": "definition", "difficulty": "easy"},
        {"category": "architecture", "difficulty": "medium"},
        {"category": "technical", "difficulty": "hard"},
    ]
)
```

### Từ Traces

```python
# Convert trace thành dataset example
client.create_example(
    dataset_name="from-traces",
    inputs={"question": trace_input},
    outputs={"answer": trace_output},
)
```

### Từ CSV/JSON

```python
import pandas as pd

df = pd.read_csv("test_data.csv")
client.create_examples(
    dataset_name="from-csv",
    inputs=df[["question"]].to_dict("records"),
    outputs=df[["answer"]].to_dict("records"),
)
```

## Dataset Types

| Type | Format | Use Case |
|------|--------|----------|
| **Input-Output** | `{input} → {output}` | QA pairs, classification |
| **Input-Only** | `{input}` | Open-ended generation |
| **Multi-turn** | `[{msg1}, {msg2}]` | Chat evaluation |
| **Conversation** | List of turns | Multi-turn agents |

## Dataset Management

```python
# List datasets
datasets = client.list_datasets()

# Get dataset
dataset = client.read_dataset(dataset_name="my-set")

# List examples
examples = client.list_examples(dataset_id=dataset.id)

# Update example
client.update_example(
    example_id="...",
    inputs={"question": "Updated question"},
    outputs={"answer": "Updated answer"},
)

# Delete
client.delete_dataset(dataset_id=dataset.id)
```

## Dataset Versioning & Tagging

Mỗi lần thêm/sửa/xoá example tạo một **version mới**. Versions có thể được tag:

```python
from datetime import datetime

# Tag version hiện tại
initial_time = datetime.now()
client.update_dataset_tag(
    dataset_name="my_dataset",
    as_of=initial_time,
    tag="prod"  # or "staging"
)

# Evaluate trên specific tagged version
from langsmith import evaluate

experiment = evaluate(
    my_chain,
    data="my_dataset:prod",  # Dùng version có tag "prod"
    # Hoặc dùng as_of:
    # data=dataset, 
    # data_config={"as_of": "prod"}
)
```

⚠️ **Important**:
- Reserved tags: `staging`, `production`
- Past versions là **immutable** (read-only)
- Promote không remove commit khỏi environment cũ
- `LangSmith Engine` có thể auto-generate ground truth từ production traces

## Three-Layer Feedback Architecture

LangSmith có 3 layers cho feedback:

```
1. Feedback Configs (org-wide schemas)
    └── 2. Queue Rubric Items (queue-specific)
            └── 3. Feedback (individual scores on runs)
```

### Feedback Config Types

```python
# Continuous (0-1)
client.create_feedback_config(
    "accuracy",
    feedback_config={
        "type": "continuous",
        "min": 0,
        "max": 1
    },
    is_lower_score_better=False
)

# Categorical
client.create_feedback_config(
    "correctness",
    feedback_config={
        "type": "categorical",
        "categories": [
            {"value": 1, "label": "Pass"},
            {"value": 0, "label": "Fail"}
        ]
    }
)

# Freeform text
client.create_feedback_config(
    "feedback",
    feedback_config={"type": "freeform"}
)
```

### Feedback Sources (4)
1. **User feedback inline** — Thumbs up/down trong UI
2. **Annotation queues** — Human reviewers với rubric
3. **Offline evaluators** — Batch evaluation experiments
4. **Online evaluators** — Production auto-evaluation

## Annotation Queues

Human reviewers workflow:

```python
# Queue có rubric, reservation, assigned reviewers
# Multi-reviewer support
# Pairwise queues: side-by-side comparison

# Tạo queue
queue = client.create_annotation_queue(
    name="quality-review",
    rubric=[
        {"key": "correctness", "type": "categorical", "options": ["Pass", "Fail"]},
        {"key": "clarity", "type": "continuous", "min": 1, "max": 5},
    ]
)
```

## Dataset Splits

```python
# Chia train/test
examples = list(client.list_examples(dataset_id="..."))
train = examples[:80]
test = examples[80:]

# Hoặc tạo nhiều datasets
client.create_dataset("train-set")
client.create_dataset("test-set")
```

## Dataset từ Production

```python
# Tạo dataset từ production traces
from datetime import datetime, timedelta

# Lấy traces từ 7 ngày qua
traces = client.list_runs(
    project_name="my-production",
    start_time=datetime.now() - timedelta(days=7),
    execution_order=1,  # Chỉ lấy run đầu tiên (user input)
)

for trace in traces:
    client.create_example(
        dataset_name="production-data",
        inputs={"question": trace.inputs["question"]},
        outputs={"answer": trace.outputs["answer"]},
    )
```

## Best Practices

1. **50-100 examples tối thiểu** — Đủ để phát hiện regression
2. **Phân loại examples** — Dùng metadata để filter (dễ/khó, loại câu hỏi)
3. **Update định kỳ** — Thêm examples từ production failures
4. **Version datasets** — Tạo dataset mới cho mỗi major version
5. **Edge cases** — Luôn có examples cho edge cases (empty input, ngôn ngữ khác)
6. **Human-verified outputs** — Output nên được domain expert kiểm tra

## Trang Liên Quan

- [Evaluation](evaluation.md) — Dùng datasets để evaluate
- [Tracing](tracing.md) — Tạo datasets từ traces
- [LangSmith Overview](langsmith-overview.md) — Tổng quan
