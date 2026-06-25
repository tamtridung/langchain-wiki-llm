---
tags: [langgraph, concept, state-graph]
created: 2026-06-25
updated: 2026-06-25
---

# StateGraph — Định Nghĩa Graph

**StateGraph** là class trung tâm của LangGraph. Nó định nghĩa luồng xử lý dưới dạng đồ thị có hướng với **state** (trạng thái) được truyền qua các **nodes**.

## Khởi Tạo StateGraph

```python
from langgraph.graph import StateGraph
from typing import TypedDict, Annotated

# 1. Định nghĩa state schema
class MyState(TypedDict):
    messages: Annotated[list, add_messages]  # Có reducer
    counter: int
    metadata: dict

# 2. Tạo graph
graph = StateGraph(MyState)
```

## Các Method Chính

| Method | Mô Tả |
|--------|-------|
| `add_node(name, func)` | Thêm node xử lý |
| `add_edge(from, to)` | Kết nối cố định giữa 2 nodes |
| `add_conditional_edges(from, router, mapping)` | Kết nối có điều kiện |
| `set_entry_point(name)` | Điểm bắt đầu của graph |
| `set_finish_point(name)` | Điểm kết thúc (ít dùng) |
| `compile(checkpointer)` | Compile graph thành app có thể chạy |

## State Schema

### 1. MessagesState (Khuyến nghị cho Agent)

```python
from langgraph.graph import MessagesState
# Tương đương:
# class MessagesState(TypedDict):
#     messages: Annotated[list, add_messages]
```

### 2. Custom State

```python
class RAGState(TypedDict):
    question: str
    documents: list[Document]
    context: str
    answer: str
```

### 3. State với Reducer

```python
from typing import Annotated
from langgraph.graph import add_messages
import operator

class AdvancedState(TypedDict):
    messages: Annotated[list, add_messages]  # Append
    total: Annotated[int, operator.add]       # Numeric add
    seen: Annotated[set, operator.or_]        # Set union
```

## Compile Graph

```python
from langgraph.checkpoint.memory import MemorySaver

# Compile với checkpointing
app = graph.compile(
    checkpointer=MemorySaver(),
    interrupt_before=["approval_node"],  # Dừng trước node này
    interrupt_after=["agent"],           # Dừng sau node này
)

# Visualize (nếu có graphviz)
from IPython.display import Image, display
display(Image(app.get_graph().draw_mermaid_png()))
```

## Graph Architecture Diagrams

LangGraph tự động sinh Mermaid diagram:

```python
# Lấy Mermaid code
print(app.get_graph().draw_mermaid())

# Draw PNG (cần pygraphviz)
app.get_graph().draw_png("graph.png")
```

## Trang Liên Quan

- [LangGraph Overview](langgraph-overview.md) — Tổng quan
- [Nodes & Edges](nodes-edges.md) — Chi tiết nodes & edges
- [Checkpointing](checkpointing.md) — Persistence
