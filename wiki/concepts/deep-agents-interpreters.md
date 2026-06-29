---
tags: [langchain, deep-agents, concept, beta]
created: 2026-06-29
updated: 2026-06-29
sources: [deep-agents-sdk]
related: [concepts/sandboxes, concepts/deep-agents-subagents, concepts/deep-agents-overview]
---

# Deep Agents — Code Interpreters

> Beta feature. Yêu cầu `langchain-quickjs>=0.1.0` và Python `>=3.11`.

Interpreters cho agent một programmable workspace — viết code để compose tools, orchestrate subagents, transform dữ liệu — mà không cần mỗi bước phải qua model reasoning.

## Why Interpreters?

| Problem | Solution |
|---------|----------|
| Model phải reasoning từng tool call | Code loop + branch + retry |
| Mọi intermediate result về model context | Intermediate values stay in variables |
| Model sample vài items thay vì all | Code processes every item deterministically |

## QuickJS Interpreter

```bash
pip install -U "deepagents[quickjs]"
```

```python
from deepagents import create_deep_agent
from langchain_quickjs import CodeInterpreterMiddleware

agent = create_deep_agent(
    model="openai:gpt-5.5",
    middleware=[CodeInterpreterMiddleware()],
)
```

Agent viết JavaScript và gọi `eval` tool. Code chạy trong **QuickJS** runtime:

```javascript
const rows = [
  { team: "alpha", score: 8 },
  { team: "beta", score: 13 },
];

const totals = rows.reduce((acc, row) => {
  acc[row.team] = (acc[row.team] ?? 0) + row.score;
  return acc;
}, {});

totals;  // Last expression = result
```

## Programmatic Tool Calling (PTC)

Expose selected tools trong interpreter dưới global `tools` namespace:

```python
agent = create_deep_agent(
    model="openai:gpt-5.5",
    middleware=[CodeInterpreterMiddleware(ptc=["web_search"])],
)
```

Agent gọi tool từ JavaScript:

```javascript
const topics = ["retrieval", "memory", "evaluation"];
const results = await Promise.all(
  topics.map(topic => tools.webSearch({ query: `${topic} best practices 2025` })),
);
results.join("\n\n");
```

Tool names → camelCase: `web_search` → `tools.webSearch(...)`.

## Dynamic Subagents từ Interpreter

Dispatch configured subagents từ code với built-in `task()` global:

```javascript
const files = ["file1.py", "file2.py", "file3.py"];
const reviews = await Promise.all(
  files.map(f => task("code-reviewer", `Review ${f}`))
);
```

## Persistence (Snapshotting)

Interpreter state persist giữa các turns trong cùng thread:

1. Turn starts → restore latest snapshot
2. Agent calls `eval` → mutate variables
3. Turn finishes → snapshot into graph state
4. Next turn → restore from snapshot

⚠️ Snapshots chỉ retain serializable values. Functions/classes không được restore.

## When to Use

| Need | Use |
|------|-----|
| 1-2 simple external calls | Normal tool calling |
| Loop, branch, retry, aggregate | **Interpreter** |
| Many tool calls từ code | **Interpreter + PTC** |
| Fan-out subagents | **Interpreter + dynamic subagents** |
| Shell, packages, filesystem | **Sandboxes** |

## Trang Liên Quan

- [Sandboxes](sandboxes.md) — Isolated code execution
- [Deep Agents Subagents](deep-agents-subagents.md) — Subagent delegation
- [Deep Agents Overview](deep-agents-overview.md) — Tổng quan Deep Agents
