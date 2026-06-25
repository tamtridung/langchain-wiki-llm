---
tags: [langsmith, source, datasets, annotation]
created: 2026-06-25
updated: 2026-06-25
sources: [raw/langchain_docs/langsmith/manage-datasets.md, raw/langchain_docs/langsmith/annotation-queues.md, raw/langchain_docs/langsmith/annotation-queues-sdk.md, raw/langchain_docs/langsmith/feedback-data-format.md]
related: [concepts/datasets, concepts/evaluation]
---

# Nguồn: LangSmith Datasets & Annotation

## Tóm Tắt

4 files về datasets và annotation queues trong LangSmith.

## Điểm Then Chốt

### Dataset Versioning
- Every add/update/delete → tạo version mới
- Tag version với semantic names (`prod`, `staging`)
- Evaluate trên specific tagged version: `list_examples(as_of=...)`
- Reserved tags: `staging` và `production`
- **Immutable khi view past versions** — read-only

### Annotation Queues
- Human reviewers workflow với rubric feedback
- **Reservation system** — tránh conflict khi nhiều reviewer
- **Assigned reviewers** — run chỉ complete khi tất cả reviewers submit
- **Multi-reviewer** support
- **Pairwise annotation queues (PAQs)** — Side-by-side comparison

### Feedback Architecture (3-layer)
1. **Feedback Configs** — Org-wide schemas (continuous 0-1, categorical Pass/Fail, freeform)
2. **Queue Rubric Items** — Queue-specific assignments
3. **Feedback** — Individual scores trên runs

### Feedback Sources
- User feedback inline
- Annotation queues
- Offline evaluators
- Online evaluators

## Code Mẫu

```python
# Dataset versioning
client.update_dataset_tag(
    dataset_name="my_dataset",
    as_of=initial_time,
    tag="prod"
)

# Feedback configs
client.create_feedback_config(
    "accuracy",
    feedback_config={
        "type": "continuous",
        "min": 0,
        "max": 1
    },
    is_lower_score_better=False
)
```

## Trang Liên Quan
- [Datasets](../concepts/datasets.md)
- [Evaluation](../concepts/evaluation.md)
