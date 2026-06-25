---
tags: [langgraph, concept, auth]
created: 2026-06-25
updated: 2026-06-25
sources: [langgraph-advanced]
related: [concepts/administration, concepts/deployment, concepts/langgraph-sdk]
---

# LangGraph Auth — Authentication & Authorization

**LangGraph Auth** (từ `langgraph_sdk.Auth`) cung cấp authentication (AuthN) và authorization (AuthZ) cho LangGraph Agent Server.

## Kiến Trúc

```
Client Request
    │
    ▼
┌──────────────────────┐
│ @auth.authenticate   │  ← AuthN: Xác thực danh tính
│ (JWT, API key, ...)  │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ @auth.on              │  ← AuthZ: Phân quyền resources
│ (handlers per type)   │
└──────────┬───────────┘
           ▼
    Graph Execution
```

## AuthN — Authentication

```python
from langgraph_sdk import Auth
from httpx import HTTPStatusError

auth = Auth()

@auth.authenticate
async def authenticate(headers: dict) -> Auth.types.MinimalUserDict:
    """Xác thực request. Trả về user info hoặc raise exception."""
    api_key = headers.get("x-api-key")
    
    if not api_key:
        raise HTTPStatusError(401, message="Missing API key")
    
    # Validate API key (gọi external service, database...)
    user = await validate_key(api_key)
    if not user:
        raise HTTPStatusError(401, message="Invalid API key")
    
    return {
        "identity": user["id"],
        "is_authenticated": True
    }
```

## AuthZ — Authorization

```python
# Resource-level access control
@auth.on
async def on_thread(thread: Auth.types.Thread, user: Auth.types.MinimalUserDict):
    """Kiểm tra quyền truy cập thread."""
    if thread["owner"] != user["identity"]:
        raise HTTPStatusError(403, message="Forbidden")

@auth.on
async def on_assistant(assistant: Auth.types.Assistant, user: Auth.types.MinimalUserDict):
    """Kiểm tra quyền truy cập assistant."""
    # Admin bypass
    if user.get("is_admin"):
        return
    if assistant["owner"] != user["identity"]:
        raise HTTPStatusError(403, message="Forbidden")
```

## Custom Auth với OAuth Provider

```python
# auth.py
from langgraph_sdk import Auth
import jwt

auth = Auth()

@auth.authenticate
async def authenticate(headers: dict) -> Auth.types.MinimalUserDict:
    token = headers.get("authorization", "").replace("Bearer ", "")
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        return {
            "identity": payload["sub"],
            "is_authenticated": True,
            "is_admin": payload.get("role") == "admin"
        }
    except jwt.InvalidTokenError:
        raise HTTPStatusError(401, message="Invalid token")
```

## Resource Ownership

```python
# Single-owner resources — chỉ owner được access
# Mặc định: user tạo resource là owner

@auth.on
async def on_resource(resource, user):
    # Chỉ owner được read/write
    if resource["owner"] != user["identity"]:
        raise HTTPStatusError(403)
```

## Production Setup

```json
// langgraph.json - auth config
{
  "graph": {
    "auth": {
      "path": "./auth.py:auth",
      "auto_register": true
    }
  }
}
```

## Best Practices

1. **AuthN trước, AuthZ sau** — Xác thực xong mới phân quyền
2. **JWT cho production** — Dùng JWT tokens thay vì hard-coded keys
3. **Resource ownership** — Luôn kiểm tra owner trước khi access
4. **Admin bypass** — Cho phép admin bypass resource-level checks
5. **Audit log** — Log tất cả auth failures

## Trang Liên Quan
- [Administration](administration.md) — Org-wide auth & RBAC
- [Deployment](deployment.md) — Deploy with auth config
- [LangGraph SDK](langgraph-sdk.md) — SDK reference
