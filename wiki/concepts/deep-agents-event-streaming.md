---
tags: [langchain, deep-agents, concept]
created: 2026-06-29
updated: 2026-06-29
sources: [deep-agents-sdk]
related: [concepts/streaming, concepts/deep-agents-subagents, concepts/deep-agents-overview]
---

# Deep Agents — Event Streaming (v3 API)

Deep Agents xây dựng trên LangGraph streaming infrastructure với first-class support cho subagent streams. Dùng **event streaming API** (`stream_events`, version v3) để consume subagent events riêng biệt.

## Stream Subagents

```python
stream = agent.stream_events({
    "messages": [{"role": "user", "content": "Write a haiku about the sea"}],
}, version="v3")

for subagent in stream.subagents:
    print(subagent.name, subagent.path, subagent.status)
    for message in subagent.messages:
        print(message.text)
```

### Subagent Stream Fields

| Field | Description |
|-------|-------------|
| `name` | Subagent name (từ `subagent_type`) |
| `messages` | Messages từ subagent |
| `subagents` | Nested subagent invocations |
| `output` | Final state / completion signal |
| `path` | Namespace path |
| `status` | `started`, `completed`, `failed`, `interrupted` |
| `tool_calls` | Tool calls trong subagent |

## Track Lifecycle

```python
for subagent in stream.subagents:
    print(f"{subagent.name}: {subagent.status}")
    try:
        _ = subagent.output
        print(f"{subagent.name}: completed")
    except Exception:
        print(f"{subagent.name}: failed")
```

## Stream Messages

```python
for message in stream.messages:
    print("[coordinator]", message.text)

for subagent in stream.subagents:
    for message in subagent.messages:
        print(f"[{subagent.name}]", message.text)
```

## Stream Tool Calls

```python
for call in stream.tool_calls:
    print("[coordinator tool]", call.tool_name, call.input)

for subagent in stream.subagents:
    for call in subagent.tool_calls:
        print(f"[{subagent.name} tool]", call.tool_name, call.input)
```

## Stream Nested Work

```python
for subagent in stream.subagents:
    for nested in subagent.subagents:
        print(f"nested {nested.name}: {nested.status}")
```

## Consume Concurrently

### Async

```python
async def consume_coordinator():
    async for message in stream.messages:
        print("[coord]", await message.text)

async def consume_subagents():
    async for subagent in stream.subagents:
        async for message in subagent.messages:
            print(f"[{subagent.name}]", await message.text)

await asyncio.gather(consume_coordinator(), consume_subagents())
```

### Sync (interleave)

```python
for name, item in stream.interleave("messages", "subagents"):
    if name == "messages":
        print("[coordinator]", item.text)
    else:
        for message in item.messages:
            print(f"[{item.name}]", message.text)
```

## Subagents vs Subgraphs

| API | Shows |
|-----|-------|
| `stream.subgraphs` | Graph execution structure (internal nodes) |
| `stream.subagents` | Product-level task delegations (user-facing) |

## Legacy Streaming (subgraph-based)

Dùng `stream_mode="updates"` với `subgraphs=True` cho streaming cơ bản:

```python
for chunk in agent.stream(
    {"messages": [...]},
    stream_mode="updates",
    subgraphs=True,
    version="v2",
):
    if not chunk["ns"]:
        print("[main agent]", chunk["data"])
    else:
        print(f"[subagent: {chunk['ns']}]", chunk["data"])
```

## Trang Liên Quan

- [Streaming](streaming.md) — LangGraph streaming concepts
- [Deep Agents Subagents](deep-agents-subagents.md) — Subagent delegation
- [Deep Agents Overview](deep-agents-overview.md) — Tổng quan Deep Agents
