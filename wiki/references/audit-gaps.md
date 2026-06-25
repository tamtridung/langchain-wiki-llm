---
tags: [langchain, reference, audit]
created: 2026-06-25
updated: 2026-06-25
---

# Audit: Concept Còn Thiếu Trong Wiki

Kết quả rà soát toàn bộ `raw/langchain_docs/` (324 files) đối chiếu với wiki hiện tại.

## Tổng Quan

| Trạng Thái | Số Lượng |
|-----------|---------|
| ✅ Đã ingest vào wiki | ~200 files (qua 11 source pages) |
| ❌ **Chưa ingest** | **~124 files** còn lại |
| 📦 Trong đó: cần tạo concept pages mới | **8 nhóm lớn** |

---

## 🟣 1. MCP (Model Context Protocol) — **Ưu tiên CAO nhất**

> **MCP** là open protocol cho phép LLMs khám phá và sử dụng tools qua structured API. Đây là concept "nóng" nhất hiện nay.

| File Gốc | Mô Tả |
|----------|-------|
| `langsmith-mcp-server.md` | (DEPRECATED) Standalone MCP server cũ |
| `langsmith-remote-mcp.md` | **Mới nhất** — Remote MCP server hosted bởi LangSmith Cloud |
| `server-mcp.md` | MCP endpoint trong Agent Server tại `/mcp` |
| `managed-deep-agents-mcp.md` | Kết nối MCP tools với Managed Deep Agents |
| `fleet/mcp-framework.md` | LangSmith Tool Server — standalone MCP framework |
| `fleet/remote-mcp-servers.md` | Kết nối Fleet tới remote MCP servers |
| `api-reference/auth-service-v2/create-mcp-oauth-provider.md` | MCP OAuth provider API |

**Cần tạo:** 1 concept page `concepts/mcp.md` + update `deployment.md` + `tools.md`

---

## 🟤 2. Fleet (~25 files) — **Ưu tiên CAO**

> Fleet là hệ thống quản lý và triển khai agent fleet — cho phép deploy agent lên Slack, Teams, web, v.v.

| Chủ Đề Con | Files |
|-----------|-------|
| **Overview & Setup** | `fleet/index.md`, `fleet/quickstart.md`, `fleet/essentials.md` |
| **Tools & Skills** | `fleet/tools.md`, `fleet/skills.md`, `fleet/mcp-framework.md` |
| **Channels** | `fleet/slack-app.md`, `fleet/teams-app.md`, `fleet/salesforce.md`, `fleet/arcade.md` |
| **Platform Features** | `fleet/computer-use.md`, `fleet/code.md`, `fleet/schedules.md`, `fleet/webhooks.md`, `fleet/channels.md`, `fleet/templates.md` |
| **Admin & Auth** | `fleet/workspace-admin.md`, `fleet/access-and-oversight.md`, `fleet/agent-identity.md`, `fleet/auth-format.md` |
| **Infrastructure** | `fleet/self-hosted-link.md`, `fleet/remote-mcp-servers.md` |
| **Reference** | `fleet/changelog.md`, `fleet/comparison.md` |

**Cần tạo:** 1 concept page `concepts/fleet.md`

---

## 🤖 3. Managed Deep Agents (~10 files + API) — **Ưu tiên CAO**

> Hosted runtime cho deep agents. Private beta, tính năng mới nhất của LangSmith.

| File Gốc | Mô Tả |
|----------|-------|
| `managed-deep-agents-overview.md` | Tổng quan |
| `managed-deep-agents-quickstart.md` | Quickstart |
| `managed-deep-agents-deploy.md` | Deploy agents |
| `managed-deep-agents-sdk.md` | Python/JS SDK |
| `managed-deep-agents-cli.md` | CLI commands |
| `managed-deep-agents-invoke.md` | Invoke patterns |
| `managed-deep-agents-mcp.md` | MCP tool integration |
| `managed-deep-agents.md` | General docs |
| `managed-deep-agents-api-overview.md` | API overview |
| `managed-deep-agents-api/` | API reference directory |

**Cần tạo:** 1 concept page `concepts/managed-deep-agents.md`

---

## 🔒 4. Sandboxes (~9 files)

> Môi trường cô lập cho evaluation & agent testing.

| File Gốc | Mô Tả |
|----------|-------|
| `sandboxes.md` | Overview |
| `sandbox-sdk.md` | Python/JS SDK |
| `sandbox-cli.md` | CLI |
| `sandbox-auth-proxy.md` | Auth proxy |
| `sandbox-permissions.md` | Permissions |
| `sandbox-mounts.md` | File mounts |
| `sandbox-snapshots.md` | Snapshots |
| `sandbox-service-urls.md` | Service URLs |
| `sandbox-harbor.md` | Harbor integration |

**Cần tạo:** 1 concept page `concepts/sandboxes.md` hoặc section trong `evaluation.md`

---

## ⚙️ 5. Engine (~5 files)

> "Agent for agent engineering" — tự động phát hiện và sửa lỗi từ production traces.

| File Gốc | Mô Tả |
|----------|-------|
| `engine.md` | Engine overview |
| `engine-overview.md` | Chi tiết |
| `engine-self-hosted.md` | Self-hosted |
| `engine-webhooks.md` | Webhooks |
| `engine-link.md` | Engine link |

**Cần tạo:** 1 concept page `concepts/engine.md`

---

## 🌐 6. LLM Gateway (~4 files)

> Proxy, redaction, spend policies cho LLM calls.

| File Gốc | Mô Tả |
|----------|-------|
| `llm-gateway.md` | Gateway overview |
| `llm-gateway-custom-providers.md` | Custom providers |
| `llm-gateway-redaction.md` | PII redaction |
| `llm-gateway-spend-policies.md` | Spend policies |

**Cần tạo:** 1 concept page `concepts/llm-gateway.md`

---

## 🧠 7. Context Engineering (~4 files)

> Skills, agents, Context Hub — versioned agent instructions & tools.

| File Gốc | Mô Tả |
|----------|-------|
| `context-engineering-concepts.md` | Concepts |
| `context-hub.md` | Context Hub |
| `manage-contexts-sdk.md` | SDK |
| `skills.md` | Skills |

**Cần tạo:** Section trong `administration.md` hoặc page riêng

---

## 🔗 8. A2A (Agent-to-Agent Protocol)

> Google's open protocol cho multi-agent communication.

| File Gốc | Mô Tả |
|----------|-------|
| `server-a2a.md` | A2A endpoint trong Agent Server |

**Cần tạo:** Section trong `multi-agent.md`

---

## 📋 9. Các File Lẻ Còn Lại (~30 files)

### OpenTelemetry
- `otel-gateway-trace-redaction.md`
- `evaluate-with-opentelemetry.md`

### Chat & Messages
- `chat-evaluation.md`, `chat-observability.md`, `chat.md`
- `messages-view-integrations.md`, `messages-view-trace-format.md`
- `multimodal-content.md`, `multiple-messages.md`

### CI/CD & Testing
- `cicd-pipeline-example.md`, `pytest.md`
- `multi-turn-simulation.md`

### Experiment & Analysis
- `analyze-an-experiment.md`, `compare-experiment-results.md`
- `experiment-configuration.md`, `filter-experiments-ui.md`
- `fetch-perf-metrics-experiment.md`, `run-backtests-new-agent.md`

### Setup & Integration
- `setup-pyproject.md`, `setup-app-requirements-txt.md`, `setup-javascript.md`
- `get-started-integrations.md`, `harbor-integrations.md`

### Config & Customization
- `configurable-headers.md`, `configurable-logs.md`
- `model-configurations.md`, `managing-model-configurations.md`
- `playground-model-providers.md`
- `custom-lifespan.md`, `custom-middleware.md`
- `generative-ui-react.md`

### Platform & Production
- `monorepo-support.md`, `serverless-environments.md`
- `shared-responsibility-model.md`, `govern.md`
- `graph-rebuild.md`, `granular-usage.md`
- `optimize-classifier.md`, `openevals.md`
- `quick-start-studio.md`, `observability-stack.md`
- `reference.md`, `rules.md`
- `local-dev-testing.md`, `local.md`
- `components.md`
- `hybrid.md`, `hybrid-legacy.md`

---

## Tổng Kết: Kế Hoạch Bổ Sung

| Ưu Tiên | Concept | Files Gốc | Trang Wiki Cần Tạo |
|----------|---------|-----------|-------------------|
| 🔴 **P1** | MCP (Model Context Protocol) | ~7 | `concepts/mcp.md` |
| 🔴 **P1** | Fleet | ~25 | `concepts/fleet.md` |
| 🔴 **P1** | Managed Deep Agents | ~10+ API | `concepts/managed-deep-agents.md` |
| 🟡 **P2** | Sandboxes | ~9 | `concepts/sandboxes.md` |
| 🟡 **P2** | Engine | ~5 | `concepts/engine.md` |
| 🟡 **P2** | LLM Gateway | ~4 | `concepts/llm-gateway.md` |
| 🟢 **P3** | Context Engineering | ~4 | Section trong `administration.md` |
| 🟢 **P3** | A2A Protocol | ~1 | Section trong `multi-agent.md` |
| 🔵 **P4** | File lẻ | ~30 | Update các trang hiện có |

**Tổng files chưa ingest:** ~124 files (38% tổng số)
