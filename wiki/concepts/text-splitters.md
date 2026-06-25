---
tags: [langchain, concept, rag, text-splitters]
created: 2026-06-25
updated: 2026-06-25
---

# Text Splitters — Chia Nhỏ Văn Bản Cho RAG

**Text Splitters** chia nhỏ documents thành các chunks để:
1. Phù hợp với context window của LLM
2. Giúp retrieval chính xác hơn (chunk quá lớn = nhiễu)
3. Tối ưu embedding quality

## Các Loại Text Splitter

### 1. RecursiveCharacterTextSplitter (Khuyến nghị)

Tự động tìm separator phù hợp: `\n\n` → `\n` → `.` → ` ` → `""`

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,       # Kích thước chunk (tokens hoặc chars)
    chunk_overlap=200,     # Overlap giữa các chunks
    length_function=len,   # Hàm đo độ dài
    separators=["\n\n", "\n", ".", " ", ""],  # Thứ tự ưu tiên separator
)

chunks = splitter.split_documents(documents)
# Hoặc split text
texts = splitter.split_text(long_text)
```

### 2. TokenTextSplitter

Chia theo số tokens (dùng tokenizer của model) — chính xác hơn character-based.

```python
from langchain_text_splitters import TokenTextSplitter

splitter = TokenTextSplitter(
    chunk_size=500,      # 500 tokens
    chunk_overlap=50,
)
```

### 3. MarkdownHeaderTextSplitter

Giữ cấu trúc Markdown — mỗi header tạo một chunk riêng.

```python
from langchain_text_splitters import MarkdownHeaderTextSplitter

headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]
splitter = MarkdownHeaderTextSplitter(headers_to_split_on)
chunks = splitter.split_text(markdown_text)
# Mỗi chunk có metadata header
```

### 4. RecursiveJsonSplitter

Chia JSON thành chunks valid, giữ cấu trúc.

```python
from langchain_text_splitters import RecursiveJsonSplitter

splitter = RecursiveJsonSplitter(max_chunk_size=2000)
chunks = splitter.split_json(json_data)
# -> List[dict] — mỗi chunk là JSON valid
```

### 5. Language-Specific Splitters

```python
from langchain_text_splitters import (
    PythonCodeTextSplitter,
    LatexTextSplitter,
    MarkdownTextSplitter,
    RecursiveCharacterTextSplitter,
)

# Tự động chọn splitter theo ngôn ngữ
splitter = RecursiveCharacterTextSplitter.from_language(
    language="python",
    chunk_size=1000,
    chunk_overlap=100,
)
```

## Chunk Size & Overlap Strategy

```
Document: [...]
                ┌──────────────────┐
Chunk 1:        |  [..........]    |  chunk_size=1000
                |      overlap     |
Chunk 2:        |    [..........]  |  chunk_overlap=200
                └──────────────────┘
```

- **Chunk nhỏ** (200-500 tokens) — Tốt cho retrieval chính xác, cần context compression
- **Chunk lớn** (1000-2000 tokens) — Tốt cho Q&A, có sẵn context đầy đủ
- **Overlap** 10-20% chunk_size — Đảm bảo không mất context ở biên

## Best Practices

1. **Luôn dùng `RecursiveCharacterTextSplitter`** trừ khi có lý do đặc biệt
2. **Chunk_size = f(context_window)** — Model 8K → chunk 2K; Model 128K → chunk 4K
3. **Metadata tracking** — Luôn giữ source metadata cho citations
4. **Chunk theo cấu trúc** — Dùng MarkdownHeaderTextSplitter cho document có cấu trúc
5. **Test chunk quality** — Mỗi chunk có đủ context để hiểu không?

## Trang Liên Quan

- [Document Loaders](document-loaders.md) — Load documents
- [Retrievers](retrievers.md) — Truy xuất chunks
- [Embeddings](embeddings.md) — Embed chunks
- [RAG](rag.md) — RAG architecture
