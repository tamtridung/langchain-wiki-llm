---
tags: [langsmith, source, sandboxes]
created: 2026-06-25
updated: 2026-06-25
sources: [raw/langchain_docs/langsmith/sandboxes.md, raw/langchain_docs/langsmith/sandbox-sdk.md, raw/langchain_docs/langsmith/sandbox-cli.md, raw/langchain_docs/langsmith/sandbox-auth-proxy.md, raw/langchain_docs/langsmith/sandbox-permissions.md, raw/langchain_docs/langsmith/sandbox-mounts.md, raw/langchain_docs/langsmith/sandbox-snapshots.md]
related: [concepts/sandboxes, concepts/evaluation]
---

# Nguồn: LangSmith Sandboxes

## Tóm Tắt

7 files về Sandboxes — môi trường cô lập cho code execution và agent testing.

## Điểm Then Chốt

### Là gì?
Sandboxes là môi trường cô lập (isolated VMs) cho agent thực thi code an toàn, không ảnh hưởng infrastructure chính. GA trên GCP US/EU/APAC và AWS US.

### Quickstart
```python
from langsmith.sandbox import SandboxClient
client = SandboxClient()
with client.sandbox() as sb:
    result = sb.run("python -c 'print(2+2)'")
    print(result.stdout)  # "4\n"
```

### Auth Proxy
- HTTP/HTTPS allowed by default, routed qua proxy để inject credentials
- Raw TCP blocked — phải allow-list explicit
- Access control: allow_list (default-deny) hoặc deny_list (default-allow)

### Permissions
- Creator: full access
- Member khác: mặc định denied, cần `sandboxes:exec` role
- Service URLs: access token riêng, không cần workspace member

### Mounts
Gắn S3 buckets, GCS buckets, Git repos vào sandbox filesystem tại `/mnt/mounts/`.

### Snapshots
Reusable filesystem bundle từ Docker image. Build từ Docker hoặc capture từ sandbox đang chạy.

## Trang Liên Quan
- [Sandboxes](../concepts/sandboxes.md)
- [Managed Deep Agents](../concepts/managed-deep-agents.md)
- [Evaluation](../concepts/evaluation.md)
