---
tags: [langchain, deep-agents, concept, beta]
created: 2026-06-29
updated: 2026-06-29
sources: [deep-agents-sdk]
related: [concepts/evaluation, concepts/deep-agents-overview, concepts/human-in-the-loop]
---

# Deep Agents — Grading Rubrics (LLM-as-a-Judge)

> Yêu cầu `deepagents>=0.6.5`. API beta.

`RubricMiddleware` cho phép agent tự đánh giá và iterate cho đến khi output đạt rubric (hoặc đạt max iterations).

## Cách Hoạt Động

```
Agent produces output
       │
       ▼
Grader sub-agent reviews output vs rubric
       │
       ├── satisfied ───────────► Done
       ├── needs_revision ──────► Agent runs again với feedback
       ├── max_iterations_reached ► Done (cap hit)
       ├── failed ──────────────► Rubric malformed
       └── grader_error ───────► Provider error
```

## Configuration

```python
from deepagents import RubricMiddleware, create_deep_agent
from langgraph.checkpoint.memory import InMemorySaver

agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    middleware=[
        RubricMiddleware(
            model="anthropic:claude-haiku-4-5",  # Smaller/cheaper grader model
            max_iterations=3,
        ),
    ],
    checkpointer=InMemorySaver(),
)
```

### Parameters

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `model` | Yes | — | Grader model (`provider:model` or `BaseChatModel`) |
| `system_prompt` | No | Built-in | Custom grading instructions |
| `tools` | No | `None` | Tools grader có thể call (run tests, count tokens) |
| `max_iterations` | No | 3 | Max iterations (max 20) |
| `on_evaluation` | No | `None` | Callback sau mỗi grading iteration |

## Pass Rubric on Invocation

```python
from langchain.messages import HumanMessage

config = {"configurable": {"thread_id": "rubric-session"}}
result = agent.invoke(
    {
        "messages": [HumanMessage("Write a haiku about spring.")],
        "rubric": (
            "- The poem has three lines\n"
            "- Lines follow a 5-7-5 syllable pattern\n"
            "- The theme is spring"
        ),
    },
    config=config,
)
```

## Observe Iteration Progress

### via Callback

```python
def log_evaluation(ev):
    print(f"iteration {ev['iteration']}: {ev['result']} — {ev['explanation']}")

RubricMiddleware(model="...", on_evaluation=log_evaluation)
```

### via Custom Events

```python
stream = agent.stream_events(input, version="v3", transformers=[CustomTransformer])

for event in stream.custom:
    if event["type"] == "rubric_evaluation_start":
        print(f"Grading iteration {event['iteration']}")
    elif event["type"] == "rubric_evaluation_end":
        print(f"Verdict: {event['result']}")
```

## Verdicts

| Status | Meaning | Loops back? |
|--------|---------|-------------|
| `satisfied` | All criteria pass | No |
| `needs_revision` | ≥1 criterion fails; feedback injected | Yes |
| `max_iterations_reached` | Cap hit | No |
| `failed` | Rubric malformed | No |
| `grader_error` | Grader exception | No |

## Trang Liên Quan

- [Evaluation](evaluation.md) — LangSmith evaluation concepts
- [Human-in-the-loop](human-in-the-loop.md) — Interrupt patterns
- [Deep Agents Overview](deep-agents-overview.md) — Tổng quan Deep Agents
