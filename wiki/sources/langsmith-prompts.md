---
tags: [langsmith, source, prompts]
created: 2026-06-25
updated: 2026-06-25
sources: [raw/langchain_docs/langsmith/create-a-prompt.md, raw/langchain_docs/langsmith/manage-prompts.md, raw/langchain_docs/langsmith/prompt-engineering.md, raw/langchain_docs/langsmith/prompt-engineering-concepts.md, raw/langchain_docs/langsmith/prompt-commit.md]
related: [concepts/prompts]
---

# Nguồn: LangSmith Prompts & Prompt Engineering

## Tóm Tắt

5 files về prompt management và prompt engineering trong LangSmith.

## Điểm Then Chốt

### Playground
- Interactive prompt editor: System/Human/AI/Tool/Chat roles
- Template variables: **f-string** (default) hoặc **mustache**
- Structured output schema, tools configuration

### Prompt Types
- **Chat prompts** (list of messages with roles) — recommended
- **Completion prompts** (single string) — legacy

### Versioning & Environments
- **Commits** — Mỗi thay đổi tạo một commit
- **Commit tags** — `staging`, `production` (reserved)
- **Promotion flow** — Promote từ Staging lên Production
- Promote không remove commit khỏi Staging — một commit có thể ở cả 2 environments

### GitHub Sync
- Webhooks trigger on prompt commit
- Ghi prompt manifests vào GitHub repo
- Cho phép CI/CD integration

### Public Prompt Hub
- Discover và share community prompts
- Pull prompt bằng tag: `client.pull_prompt("joke-generator:production")`

### Prompt Owners
- Fine-grained access control
- Ai có thể tag/delete/promote prompts

## Trang Liên Quan
- [Prompts](../concepts/prompts.md)
- [LangSmith Overview](../concepts/langsmith-overview.md)
