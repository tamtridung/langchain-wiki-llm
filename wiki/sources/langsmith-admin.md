---
tags: [langsmith, source, administration]
created: 2026-06-25
updated: 2026-06-25
sources: [raw/langchain_docs/langsmith/auth.md, raw/langchain_docs/langsmith/authentication-methods.md, raw/langchain_docs/langsmith/admin.md, raw/langchain_docs/langsmith/administration-overview.md, raw/langchain_docs/langsmith/rbac.md, raw/langchain_docs/langsmith/audit-logs.md, raw/langchain_docs/langsmith/billing.md, raw/langchain_docs/langsmith/manage-organization-by-api.md, raw/langchain_docs/langsmith/organization-workspace-operations.md]
related: [concepts/langsmith-overview]
---

# Nguồn: LangSmith Administration & Auth

## Tóm Tắt

9 files về administration, authentication, authorization, và organization management trong LangSmith.

## Điểm Then Chốt

### Authentication
- **AuthN** (`@auth.authenticate`) vs **AuthZ** (`@auth.on` handlers)
- Cloud: API keys mặc định
- Self-hosted: không có auth mặc định — custom auth handlers via LangGraph SDK `Auth` class
- Cloud methods: Email/password, GitHub, Google, SAML SSO (Enterprise)
- Self-hosted: SSO OAuth 2.0/OIDC, basic auth

### Resource Hierarchy
**Organization → Workspace(s) → Application(s) → Resources**
- Billing/plans: Organization level
- Tracing projects/datasets/prompts: Workspace hoặc Application level

### RBAC
- 4 org roles: **Admin, Operator, User, Viewer**
- Custom workspace roles (Enterprise)
- Granular permissions: `organization:manage`, `organization:read`, `organization:pats:create`
- SCIM groups + SSO Groups Sync

### Audit Logs (Enterprise)
- Track ai xoá cái gì, khi nào
- 400-day retention
- OCSF v1.7.0 format (SIEM-friendly)

### Billing
- Developer: 5K traces/month (free)
- Plus: 10K traces
- Enterprise: custom
- Spend limits, data retention caps

### Terraform Support
- Full org management via REST API + Terraform provider for IaC

## Trang Liên Quan
- [LangSmith Overview](../concepts/langsmith-overview.md)
