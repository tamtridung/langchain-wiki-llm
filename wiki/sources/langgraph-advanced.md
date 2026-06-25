---
tags: [langgraph, source, sdk, store, functional-api]
created: 2026-06-25
updated: 2026-06-25
sources: [raw/langchain_docs/langsmith/langgraph-python-sdk.md, raw/langchain_docs/langsmith/langgraph-js-ts-sdk.md, raw/langchain_docs/langsmith/deploy-other-frameworks.md, raw/langchain_docs/langsmith/agent-server-api/store/*, raw/langchain_docs/langsmith/auth.md, raw/langchain_docs/langsmith/resource-auth.md, raw/langchain_docs/langsmith/set-up-custom-auth.md]
related: [concepts/langgraph-sdk, concepts/langgraph-store, concepts/langgraph-functional-api, concepts/langgraph-auth]
---

# Nguồn: LangGraph SDK, Store, Functional API & Auth

## Tóm Tắt

Tổng hợp các file về LangGraph SDK (Python + JS/TS), Store, Functional API, và Authentication.

## LangGraph Python SDK

- PyPI: `langgraph-sdk` 
- Core import: `from langgraph_sdk import get_client`
- Auto-connects tới `http://localhost:8123` (local) hoặc custom URL
- Sub-clients: `client.assistants`, `client.threads`, `client.runs`, `client.crons`
- Thread-Centric Streaming (v3) — `client.threads.stream()` với typed projections

## LangGraph JS/TS SDK

- npm: `@langchain/langgraph-sdk`
- Sub-clients: `client.threads`, `client.assistants`, `client.runs`, `client.crons`, `client.store`
- Framework adapters: React, Vue, Svelte, Angular
- Transport: SSE (default), WebSocket

## Functional API

- Dùng `@task` và `@entrypoint` decorators
- Cho phép deploy Claude Agent SDK, Strands, CrewAI, AutoGen lên Agent Server
- Entrypoint nhận `previous` state, trả `entrypoint.final(value=..., save=...)`

## Trang Liên Quan
- [LangGraph SDK](../concepts/langgraph-sdk.md)
- [LangGraph Store](../concepts/langgraph-store.md)
- [LangGraph Auth](../concepts/langgraph-auth.md)
