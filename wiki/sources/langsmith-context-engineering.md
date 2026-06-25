---
tags: [langsmith, source, context-engineering]
created: 2026-06-25
updated: 2026-06-25
sources: [raw/langchain_docs/langsmith/context-engineering-concepts.md, raw/langchain_docs/langsmith/context-hub.md, raw/langchain_docs/langsmith/manage-contexts-sdk.md, raw/langchain_docs/langsmith/skills.md]
related: [concepts/administration, concepts/fleet]
---

# Nguồn: Context Engineering & Skills

## Tóm Tắt

4 files về Context Engineering — versioned agent instructions, skills, và Context Hub.

## Điểm Then Chốt

### Context Engineering
Quản lý agent configuration dưới dạng versioned "contexts". Mỗi context là bundle gồm instructions, tools, skills.

### Context Hub
- Version-controlled repository cho agent instructions/tools
- Hỗ trợ environment promotion (dev → staging → production)
- Tích hợp với Managed Deep Agents

### Skills
- Reusable capability bundles (`SKILL.md` format)
- Loaded vào long-term memory của agent
- Hai loại: Private (1 agent) và Shared (tất cả agents trong workspace)
- Follow [Agent Skills specification](https://agentskills.io/specification)

## Trang Liên Quan
- [Administration](../concepts/administration.md)
- [Fleet](../concepts/fleet.md)
- [Managed Deep Agents](../concepts/managed-deep-agents.md)
