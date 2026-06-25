---
tags: [langsmith, concept, sandboxes]
created: 2026-06-25
updated: 2026-06-25
sources: [langsmith-sandboxes]
related: [concepts/evaluation, concepts/managed-deep-agents]
---

# Sandboxes — Môi Trường Cô Lập Cho Code Execution

**Sandboxes** là môi trường VM cô lập cho agent thực thi code an toàn, không ảnh hưởng infrastructure chính. GA trên GCP US/EU/APAC và AWS US.

## Quickstart

```python
from langsmith.sandbox import SandboxClient

client = SandboxClient()

with client.sandbox() as sb:
    result = sb.run("python -c 'print(2 + 2)'")
    print(result.stdout)  # "4\n"
    
    # Install packages
    sb.run("pip install requests")
    
    # Run scripts
    result = sb.run("python script.py")
```

## Auth Proxy

Inject credentials vào outbound requests và kiểm soát destinations:

```python
from langsmith.sandbox import mount_config, aws_auth, s3_mount

mount_cfg = mount_config(
    auth=[aws_auth(
        access_key_id=workspace_secret("AWS_ACCESS_KEY_ID"),
        secret_access_key=workspace_secret("AWS_SECRET_ACCESS_KEY"),
    )],
    mounts=[s3_mount(
        id="customer_data",
        mount_path="/mnt/mounts/customer-data",
        bucket="my-bucket",
        read_only=True,
    )],
)
```

- HTTP/HTTPS: allowed by default, routed qua proxy
- Raw TCP: blocked, phải allow-list explicit
- Access control: allow_list (default-deny) hoặc deny_list (default-allow)

## CLI

```bash
# Create sandbox
langsmith sandbox create my-vm --vcpus 2 --memory 1gb --wait

# Execute command
langsmith sandbox exec my-vm -- python --version

# Build snapshot from Docker image
langsmith sandbox snapshot build my-snapshot \
  --docker-image ubuntu:24.04 --capacity 8gb --wait

# Delete
langsmith sandbox delete my-vm
```

## Snapshots

Reusable filesystem bundles từ Docker images:

```python
# Build từ Docker image
snapshot = client.create_snapshot(
    "python",
    docker_image="python:3.12-slim",
    fs_capacity_bytes=1_073_741_824
)

# Capture từ sandbox đang chạy
snapshot = client.create_snapshot("state-a", source_sandbox_id=sb.id)
```

## Permissions

| Caller | Mặc định | Với `sandboxes:exec` |
|--------|---------|---------------------|
| Creator | ✅ Full | ✅ Full |
| Member khác | ❌ Denied | ✅ Allowed |
| Workspace khác | ❌ 404 | ❌ 404 |

## Use Cases

- **Evaluation** — Chạy code evaluators trong môi trường cô lập
- **Managed Deep Agents** — Sandbox backend cho code execution
- **Data processing** — Chạy scripts an toàn, không ảnh hưởng host
- **Multi-tenant** — Mỗi user/thread có sandbox riêng

## Trang Liên Quan
- [Managed Deep Agents](managed-deep-agents.md) — Deep Agents với sandbox backend
- [Evaluation](evaluation.md) — Code evaluators
