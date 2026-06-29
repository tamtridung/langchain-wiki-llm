---
tags: [langchain, deep-agents, reference]
created: 2026-06-29
updated: 2026-06-29
sources: [deep-agents-sdk]
related: [concepts/deep-agents-overview, concepts/deep-agents-production]
---

# So Sánh: Deep Agents vs Claude Agent SDK

| Tiêu Chí | **Deep Agents** | **Claude Agent SDK** |
|----------|-----------------|----------------------|
| **Where agent runs** | Inside sandbox OR outside (sandbox as tool) | Inside sandbox |
| **Execution backend** | Pluggable: local, VFS, remote sandbox, custom | Sandbox local filesystem |
| **Model provider** | Any (100+): OpenAI, Anthropic, Google, open-weight... | Claude-only (Anthropic, Bedrock, Vertex, Azure) |
| **Per-model tuning** | Harness profiles (declarative, registered per provider/model) | Configure in code |
| **Deployment** | Managed (LangSmith) + Self-hosted (Docker) | Self-hosted (build server + auth + streaming) |
| **Multi-tenancy** | Built-in: scoped threads, per-user sandboxes, RBAC | Build yourself |
| **License** | MIT | MIT (Claude Code proprietary) |
| **Ecosystem** | LangChain + LangSmith (observability, evaluation, deployment) | Anthropic product surface |

## Main Differences

### 1. Agent & Execution Environment

Deep Agents supports **2 patterns**:
- **Agent inside sandbox** (same as Claude Agent SDK)
- **Sandbox as tool** — agent in long-lived container, executes commands remotely

Claude Agent SDK chỉ support pattern 1.

### 2. Multi-Tenancy

Claude Agent SDK: bạn tự build API wrapper để quản lý sandbox per user.
Deep Agents: built-in per-user sandbox, scoped threads, RBAC, auth proxy.

### 3. Production Agent Server

Claude Agent SDK: bạn tự build HTTP/WebSocket server.
Deep Agents: includes agent server out-of-the-box (streaming, threads, webhooks, auth).

### 4. Managed vs Self-Hosted

Claude Agent SDK: self-hosted only. SDK và managed agents là products riêng.
Deep Agents: code không đổi, chạy được cả managed + self-hosted.

## Summary

- **Chọn Deep Agents** nếu: cần model flexibility, built-in multi-tenant deployment, managed hoặc self-hosted
- **Chọn Claude Agent SDK** nếu: đã đầu tư vào Anthropic ecosystem, muốn tự build API/auth/multi-tenant

## Trang Liên Quan

- [Deep Agents Overview](deep-agents-overview.md) — Tổng quan Deep Agents
- [Deep Agents Production](deep-agents-production.md) — Production deployment
- [Managed Deep Agents](managed-deep-agents.md) — Hosted runtime
