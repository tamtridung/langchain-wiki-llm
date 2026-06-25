---
tags: [langgraph, concept, sdk]
created: 2026-06-25
updated: 2026-06-25
sources: [langgraph-advanced]
related: [concepts/state-graph, concepts/streaming, concepts/human-in-the-loop]
---

# LangGraph SDK — Tương Tác Với LangGraph API

**LangGraph SDK** cho phép Python và JS/TS apps kết nối đến LangGraph API Server để quản lý assistants, threads, runs, và schedules.

## Python SDK

### Cài Đặt

```bash
pip install langgraph-sdk
# hoặc: uv add langgraph-sdk
```

### Quick Start

```python
from langgraph_sdk import get_client

# Tự động kết nối http://localhost:8123 (langgraph dev)
client = get_client()

# Hoặc remote server
client = get_client(
    url="https://my-agent.langgraph.app",
    api_key="lsv2_pt_..."
)

# List assistants
assistants = await client.assistants.search()
agent = assistants[0]

# Tạo thread
thread = await client.threads.create()

# Stream run
async for chunk in client.runs.stream(
    thread['thread_id'],
    agent['assistant_id'],
    input={"messages": [{"role": "human", "content": "Hello!"}]}
):
    print(chunk)
```

### Sub-clients

| Sub-client | Mục Đích |
|------------|----------|
| `client.assistants` | CRUD assistants, graph schemas, versions |
| `client.threads` | Tạo threads, manage state, **stream** runs |
| `client.runs` | Trigger/join/cancel runs (legacy) |
| `client.crons` | Schedule recurring runs |

### Thread-Centric Streaming (v3)

```python
async with client.threads.stream(
    thread_id="my-thread",
    assistant_id="agent",
) as thread:
    await thread.run.start(
        input={"messages": [{"role": "user", "content": "hi"}]}
    )
    
    # Typed projections - share 1 SSE connection
    async for msg in thread.messages:
        print(await msg.text)
    
    final = await thread.output  # terminal state
```

**Projections:** `thread.messages`, `thread.tool_calls`, `thread.values`, `thread.output`, `thread.interrupts`, `thread.subgraphs`

### Known Limitations
- WebSocket cần `websockets>=14`
- Sync streaming dùng background thread
- Max 5 reconnect attempts

## JS/TS SDK (Tham Khảo)

```typescript
import { Client } from "@langchain/langgraph-sdk";

const client = new Client({ apiUrl: "http://localhost:2024" });
const thread = client.threads.stream({ assistantId: "my-agent" });

await thread.run.start({
  input: { messages: [{ role: "user", content: "hello" }] },
});

for await (const message of thread.messages) {
  for await (const token of message.text) {
    process.stdout.write(token);
  }
}
```

### Framework Adapters
- `@langchain/langgraph-sdk/react` — React hooks
- `@langchain/langgraph-sdk/vue` — Vue composables
- `@langchain/langgraph-sdk/svelte` — Svelte stores
- `@langchain/langgraph-sdk/angular` — Angular services

## Best Practices

1. **Luôn dùng Thread-Centric Streaming (v3)** — `client.threads.stream()` thay vì legacy `client.runs.stream()`
2. **Typed projections** — Dùng `thread.messages`, `thread.tool_calls` thay vì parse raw events
3. **Async all the way** — SDK async-first, dùng `asyncio.gather()` cho nhiều projections
4. **Error handling** — Catch `RuntimeError` trên reconnect failures
5. **API key** — Dùng `lsv2_pt_...` format cho remote servers

## Trang Liên Quan
- [LangGraph Overview](langgraph-overview.md)
- [StateGraph](state-graph.md)
- [Streaming](streaming.md)
- [Human-in-the-loop](human-in-the-loop.md)
