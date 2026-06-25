---
tags: [langsmith, concept, administration]
created: 2026-06-25
updated: 2026-06-25
sources: [langsmith-admin]
related: [concepts/langsmith-overview]
---

# Administration — Quản Trị LangSmith

**Administration** trong LangSmith bao gồm authentication, authorization, organization management, và security.

## Resource Hierarchy

```
Organization (Billing, Plans)
    └── Workspace(s) (Tracing projects, datasets, prompts)
            └── Application(s) (Deployments, agents)
                    └── Resources (Runs, traces)
```

## Authentication Methods

| Method | Cloud | Self-hosted |
|--------|-------|-------------|
| Email/Password | ✅ | ❌ |
| GitHub OAuth | ✅ | ❌ |
| Google OAuth | ✅ | ❌ |
| SAML SSO | ✅ (Enterprise) | ❌ |
| OAuth 2.0/OIDC | ❌ | ✅ |
| Basic Auth | ❌ | ✅ (deprecated) |
| API Keys | ✅ | ✅ |
| Custom Auth | ✅ (LangGraph SDK) | ✅ |

## RBAC — Role-Based Access Control

### Organization Roles (4)
| Role | Quyền Hạn |
|------|-----------|
| **Admin** | Full access, billing, invite admins |
| **Operator** | Day-to-day ops, không invite/modify admins |
| **User** | Works within assigned resources |
| **Viewer** | Read-only |

### Granular Permissions
```python
# Permission format: {resource}:{action}
"organization:manage"       # Quản lý tổ chức
"organization:read"         # Đọc thông tin
"organization:pats:create"  # Tạo Personal Access Tokens
"workspace:manage"          # Quản lý workspace
```

### Enterprise Features
- Custom workspace roles
- SCIM groups integration
- SSO Groups Sync — tự động gán role dựa trên group

## Audit Logs (Enterprise)

```bash
curl -G 'https://api.smith.langchain.com/api/v1/audit-logs' \
  -H 'X-API-Key: lsv2_sk_...' \
  -d 'limit=2' \
  --data-urlencode 'start_time=2026-01-01T18:35:16.232Z'
```

- Track ai xoá/action gì, khi nào
- 400-day retention
- OCSF v1.7.0 format — tương thích SIEM

## Billing Plans

| Plan | Traces | Key Features |
|------|--------|-------------|
| **Developer** | 5K/month (free) | 1 project, basic tracing |
| **Plus** | 10K | Unlimited projects, annotations |
| **Enterprise** | Custom | SSO, self-hosted, audit logs |

## Custom Auth Handlers (LangGraph SDK)

```python
from langgraph_sdk import Auth

auth = Auth()

@auth.authenticate
async def authenticate(headers: dict) -> Auth.types.MinimalUserDict:
    # Validate credentials
    api_key = headers.get("x-api-key")
    if not is_valid(api_key):
        raise HTTPException(status_code=401)
    return {"identity": "user_123"}
```

## Terraform Integration

```bash
# Quản lý LangSmith resources với IaC
terraform {
  required_providers {
    langsmith = {
      source = "langchain/langsmith"
    }
  }
}
```

## Context Engineering

**Context Engineering** quản lý agent configuration dưới dạng versioned "contexts":

### Context Hub
Version-controlled repository cho agent instructions/tools:
- Mỗi context = bundle (instructions + tools + skills)
- Environment promotion: dev → staging → production
- Tích hợp với Managed Deep Agents

### Skills
Reusable capability bundles (`SKILL.md` format):
```markdown
# SKILL.md
## Description
When to use this skill - write as instructions, not labels.

## Instructions
How the agent should behave when using this skill.
```
- Loaded vào long-term memory của agent
- **Private**: 1 agent
- **Shared**: Tất cả agents trong workspace, auto-sync
- Follow [Agent Skills specification](https://agentskills.io/specification)

## Best Practices

1. **Least privilege** — Chỉ gán permissions cần thiết
2. **API keys rotation** — Rotate keys định kỳ
3. **Audit logs monitoring** — Phát hiện hành vi bất thường
4. **SSO cho Enterprise** — Centralized identity management
5. **Workspace isolation** — Mỗi team/ project một workspace riêng
6. **Context versioning** — Dùng Context Hub cho mọi agent config

## Trang Liên Quan
- [LangSmith Overview](langsmith-overview.md) — Tổng quan
- [Deployment](deployment.md) — Deployment & self-hosted
- [Fleet](fleet.md) — Fleet platform
- [Managed Deep Agents](managed-deep-agents.md) — Deep Agents
