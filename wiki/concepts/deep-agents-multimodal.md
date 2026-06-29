---
tags: [langchain, deep-agents, concept]
created: 2026-06-29
updated: 2026-06-29
sources: [deep-agents-sdk]
related: [concepts/deep-agents-context-engineering, concepts/deep-agents-backends]
---

# Deep Agents — Multimodal I/O

Deep Agents hỗ trợ multimodal workflows khi model hỗ trợ multimodal inputs và tool results.

## Multimodal User Input

```python
result = agent.invoke({
    "messages": [{
        "role": "user",
        "content": [
            {"type": "text", "text": "What is in this screenshot?"},
            {"type": "image", "url": "https://example.com/screenshot.png"},
        ],
    }],
})
```

## Built-in `read_file` Support

`read_file` trả về standard content blocks cho multimodal files:

| Type | Extensions |
|------|-----------|
| Image | `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.heic`, `.heif` |
| Video | `.mp4`, `.mpeg`, `.mov`, `.avi`, `.flv`, `.webm`, `.wmv`, `.3gpp` |
| Audio | `.wav`, `.mp3`, `.aiff`, `.aac`, `.ogg`, `.flac` |
| File | `.pdf`, `.ppt`, `.pptx` |

## Custom Tool Outputs

Tools có thể return multimodal content:

```python
from langchain.tools import tool

@tool
def capture_screenshot() -> list[dict]:
    """Capture a screenshot of the current page."""
    return [
        {"type": "text", "text": "Screenshot of the current page:"},
        {"type": "image", "url": "https://example.com/page.png"},
    ]
```

## Context Compression & Multimodal

- **Offloading** — chỉ đếm text tokens, non-text blocks preserved
- **Summarization** — compact messages cũ thành text-only summary; image/audio/video blocks không carry forward

Best practices cho multimodal-heavy workloads:
1. Store images trong filesystem backend, pass file paths/URLs
2. Prefer references over base64 trong long-running conversations
3. Dùng subagents cho image-heavy inspection
4. Tune summarization thresholds nếu provider tính nhiều tokens cho images

## Trang Liên Quan

- [Deep Agents Context Engineering](deep-agents-context-engineering.md) — Context compression
- [Deep Agents Backends](deep-agents-backends.md) — Filesystem backends
