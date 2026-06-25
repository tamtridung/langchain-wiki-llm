# LangChain Wiki — CLAUDE.md

File này định nghĩa cách Claude Code duy trì **LangChain Wiki** — kho kiến thức toàn diện về **LangChain ecosystem** (LangChain, LangGraph, LangSmith) giúp người dùng trở thành chuyên gia xây dựng AI Agent với Python.

**Người dùng:** Python developer, muốn đạt trình độ 10+ năm kinh nghiệm về AI Agent development.
**Mục tiêu:** Wiki bao phủ toàn bộ LangChain stack — từ core framework, LCEL, RAG, tools, agent patterns, LangGraph (stateful orchestration), đến LangSmith (observability, evaluation, deployment).

## Cấu Trúc Thư Mục

```
Langchain-wiki/
├── CLAUDE.md              ← File này. Schema & quy ước cho LangChain Wiki.
├── raw/                   ← Tài liệu nguồn bất biến
│   ├── langchain_docs/
│   │   ├── api-reference/ ← API references (agent-connections, auth, deployments, integrations, listeners)
│   │   └── langsmith/     ← LangSmith documentation (tracing, evaluation, datasets, deployment, v.v.)
├── wiki/                  ← Wiki do LLM tạo ra (Claude viết; bạn đọc)
│   ├── index.md           ← Danh mục tổng thể tất cả các trang
│   ├── log.md             ← Nhật ký theo thời gian, chỉ thêm vào cuối
│   ├── overview.md        ← Tổng quan hệ sinh thái LangChain (4-layer: LangChain, LangGraph, LangSmith, LangServe)
│   ├── entities/          ← Thực thể (Harrison Chase, LangChain Inc.)
│   ├── concepts/          ← Khái niệm then chốt (chia theo nhóm)
│   │   ├── langchain-core.md      ← Framework nền tảng
│   │   ├── lcel.md                ← LangChain Expression Language
│   │   ├── runnables.md           ← Runnable interface
│   │   ├── prompts.md             ← Prompt templates
│   │   ├── chat-models.md         ← Chat models
│   │   ├── output-parsers.md      ← Output parsers
│   │   ├── tools.md               ← Tools & function calling
│   │   ├── memory.md              ← Memory systems
│   │   ├── callbacks.md           ← Callbacks & event system
│   │   ├── document-loaders.md    ← Document loaders
│   │   ├── text-splitters.md      ← Text splitters
│   │   ├── embeddings.md          ← Embeddings
│   │   ├── vector-stores.md       ← Vector stores
│   │   ├── retrievers.md          ← Retrievers
│   │   ├── rag.md                 ← RAG architecture
│   │   ├── agent-architectures.md ← Agent patterns
│   │   ├── create-agent.md        ← create_agent harness
│   │   ├── langgraph-overview.md  ← LangGraph overview
│   │   ├── state-graph.md         ← StateGraph
│   │   ├── nodes-edges.md         ← Nodes & edges
│   │   ├── checkpointing.md       ← Checkpointing & persistence
│   │   ├── streaming.md           ← Streaming
│   │   ├── human-in-the-loop.md   ← Human-in-the-loop
│   │   ├── multi-agent.md         ← Multi-agent systems
│   │   ├── langsmith-overview.md  ← LangSmith overview
│   │   ├── tracing.md             ← Tracing & observability
│   │   ├── evaluation.md          ← Evaluation (offline/online, agent eval, graph eval)
│   │   ├── datasets.md            ← Datasets (versioning, tagging, feedback arch.)
│   │   ├── monitoring.md          ← Monitoring (alerts, dashboards, cost, insights)
│   │   ├── administration.md      ← Administration (auth, RBAC, audit logs, billing, context eng.)
│   │   ├── mcp.md                 ← MCP protocol
│   │   ├── fleet.md               ← Fleet no-code agent platform
│   │   ├── managed-deep-agents.md ← Hosted deep agents runtime
│   │   ├── sandboxes.md           ← Isolated code execution envs
│   │   ├── engine.md              ← Auto-fix engine
│   │   ├── llm-gateway.md         ← LLM proxy & spend control
│   │   └── deployment.md          ← LangServe, Agent Server, self-hosted, cron
│   ├── sources/           ← 19 trang tóm tắt nguồn từ raw/ (tổng hợp ~324 file LangSmith + 39 API endpoints)
│   │   ├── langsmith-observability.md
│   │   ├── langsmith-evaluation.md
│   │   ├── langsmith-deployment.md
│   │   ├── langsmith-datasets-annotation.md
│   │   ├── langsmith-selfhosted.md
│   │   ├── langsmith-prompts.md
│   │   ├── langsmith-production.md
│   │   ├── langsmith-advanced.md
│   │   ├── langsmith-admin.md
│   │   ├── langsmith-data-management.md
│   │   └── api-reference.md
│   └── references/        ← Tài liệu tham khảo (so sánh, cheat sheets, v.v.)
```

## Quy Ước

### Tags cho YAML Frontmatter

```yaml
---
tags: [langchain, concept, <nhom-con>]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [source-slug-1]
related: [concept/ten-khai-niem, entity/ten-thuc-the]
---
```

Các tag sử dụng:
- **Nhóm 1: Ecosystem** — `langchain`, `langgraph`, `langsmith`, `langserve`
- **Nhóm 2: Domain** — `core`, `agent`, `rag`, `observability`, `evaluation`, `deployment`
- **Nhóm 3: Type** — `concept`, `entity`, `reference`, `source`, `tutorial`

> **⚠️ YAML format:** Trong `related` và `sources` fields, dùng plain YAML list syntax `[Page1, Page2]` — **không** dùng wikilinks `[[Page1]]`. Wikilinks chỉ dùng trong **body markdown**, không trong YAML frontmatter.

### Liên kết nội bộ

Sử dụng markdown link chuẩn, đường dẫn tương đối:

```markdown
[LangChain Core](../concepts/langchain-core.md)
[LCEL](../concepts/lcel.md)
[Harrison Chase](../entities/harrison-chase.md)
```

### Code Examples

Vì người dùng Python, tất cả code examples dùng Python. Ưu tiên:
- Type hints đầy đủ
- Async patterns khi production
- Import từ `langchain_core` thay vì `langchain` (trừ community integrations)

## Quy Trình Làm Việc (Workflows)

### 1. NẠP (INGEST) một nguồn mới

Khi người dùng thả nguồn mới vào `raw/` và yêu cầu xử lý:

1. **Đọc file nguồn** từ `raw/`. Dùng `markitdown-mcp` nếu available, nếu không dùng skills phù hợp.
2. **Thảo luận** với người dùng về điểm nhấn — do chủ đề rộng (LangChain ecosystem), cần xác định:
   - Nguồn này thuộc component nào? (LangChain core? LangGraph? LangSmith?)
   - Có ảnh hưởng đến trang nào hiện có không?
   - Cần tạo thực thể/khái niệm mới không?
3. **Tạo/update các trang:**
   - `wiki/sources/<slug>.md` — Tóm tắt nguồn
   - `wiki/entities/` — Cập nhật thực thể liên quan
   - `wiki/concepts/` — Cập nhật khái niệm liên quan
   - `wiki/overview.md` — Nếu có thay đổi lớn
   - `wiki/index.md` — Luôn cập nhật
   - `wiki/log.md` — Luôn ghi log
4. **Cập nhật `CLAUDE.md`** — Cập nhật sơ đồ cấu trúc thư mục nếu thêm concept/entity mới.

### 2. TRUY VẤN (QUERY) wiki

Khi người dùng hỏi về LangChain/LangGraph/LangSmith:

1. Đọc `wiki/index.md` để định vị trang liên quan
2. Đọc các trang đó
3. Tổng hợp câu trả lời kèm trích dẫn và code examples Python
4. Nếu câu trả lời quan trọng, đề xuất tạo trang reference/so sánh mới

### 3. KIỂM TRA (LINT) wiki

- 🔴 **Mâu thuẫn** — Các trang nói trái ngược nhau về cùng concept
- 🟡 **Tuyên bố lỗi thời** — LangChain thay đổi nhanh (vd: `LLMChain` deprecated, chuyển sang LCEL)
- 🟠 **Trang mồ côi** — Trang không có link từ trang nào khác
- 🔵 **Trang thiếu** — Concept quan trọng chưa có trang (vd: `langserve`, `evaluation`)
- ⚪ **Thiếu liên kết chéo** — Các concept liên quan chưa link với nhau

### 4. DUY TRÌ (MAINTAIN) index & structure

Mỗi khi tạo/cập nhật trang, cập nhật `wiki/index.md`. Giữ index có tổ chức theo danh mục.

Cập nhật sơ đồ cấu trúc thư mục trong file này khi thêm concept/entity mới.

## Hướng Dẫn Văn Phong Cho LangChain Wiki

- **Ngôn ngữ:** Tiếng Việt
- **Giọng văn:** Trung lập, chuyên gia, kèm code examples Python thực tế
- **Code examples:** Luôn dùng Python, ưu tiên `langchain_core` imports, async patterns
- **So sánh:** Khi có nhiều cách (vd: PydanticOutputParser vs with_structured_output), trình bảng so sánh
- **Heading:** `##` cho section chính, `###` cho subsection, `####` cho sub-subsection
- **Đoạn văn:** 2-4 câu, súc tích
- **In đậm:** Cho thuật ngữ lần đầu xuất hiện trong trang
- **Cập nhật:** LangChain thay đổi theo từng release — ghi chú version khi nói về feature cụ thể

## Pipeline Nạp Hàng Loạt LangSmith Docs

`raw/langchain_docs/langsmith/` chứa ~200+ file Markdown về LangSmith. Khi xử lý:

1. Gom theo chủ đề: Tracing, Evaluation, Datasets, Deployment, Self-hosted, API
2. Hỏi người dùng muốn xử lý chủ đề nào trước
3. Mỗi chủ đề tạo: 1 source page tổng hợp + update các concept pages liên quan

## Kiến Trúc Tham Chiếu Nhanh

```
┌──────────────────────────────────────────────────────┐
│                    LangChain Core                     │
│  Runnable | LCEL | Prompts | Models | Parsers        │
│  Memory | Tools | Callbacks | Retrievers             │
├──────────────────────────────────────────────────────┤
│                     LangGraph                         │
│  StateGraph | Nodes/Edges | Checkpointing            │
│  Streaming | HIL | Multi-Agent                       │
├───────────────────────────┬──────────────────────────┤
│       LangSmith           │       LangServe          │
│  Tracing | Evaluation     │  Deployment | REST API   │
│  Datasets | Monitoring    │  Streaming | Monitoring  │
└───────────────────────────┴──────────────────────────┘
```

## Pipeline Xử Lý Câu Hỏi

Khi người dùng hỏi về LangChain:

1. Xác định chủ đề thuộc layer nào (Core, Graph, Smith, Serve)
2. Tra `wiki/index.md` → tìm concept pages
3. Đọc concept pages + source pages liên quan
4. Trả lời kèm:
   - Code Python mẫu (chạy được ngay)
   - Link đến trang wiki liên quan
   - Best practices từ kinh nghiệm 10+ năm
5. Đề xuất tạo thêm reference/concept page nếu cần
