---
tags: [langchain, concept, core, rag]
created: 2026-06-25
updated: 2026-06-25
---

# Embeddings — Chuyển Văn Bản Thành Vector

**Embeddings** là các mô hình chuyển đổi văn bản thành vector số học. Vector này capture ý nghĩa ngữ nghĩa của văn bản — các câu có nghĩa tương tự sẽ có vector gần nhau trong không gian.

## Interface

```python
from langchain_core.embeddings import Embeddings

class MyEmbeddings(Embeddings):
    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        """Embed multiple documents (batch)."""
        pass

    def embed_query(self, text: str) -> list[float]:
        """Embed a single query (thường khác với documents)."""
        pass
```

## Các Provider Phổ Biến

```python
# OpenAI
from langchain_openai import OpenAIEmbeddings
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
# dimensions: 1536 (small), 3072 (large)
# text-embedding-3-small: 1536 dims, tốt cho speed/cost
# text-embedding-3-large: 3072 dims, tốt cho accuracy

# Ollama (local)
from langchain_ollama import OllamaEmbeddings
embeddings = OllamaEmbeddings(model="nomic-embed-text")

# Hugging Face (local)
from langchain_huggingface import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Google
from langchain_google_genai import GoogleGenerativeAIEmbeddings
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# Cohere
from langchain_cohere import CohereEmbeddings
embeddings = CohereEmbeddings(model="embed-english-v3.0")
```

## Cache Embeddings

Tránh embed lại cùng văn bản:

```python
from langchain_community.embeddings import CacheBackedEmbeddings
from langchain.storage import LocalFileStore

store = LocalFileStore("./embedding_cache/")
cached_embeddings = CacheBackedEmbeddings.from_bytes_store(
    underlying_embeddings=embeddings,
    document_embedding_cache=store,
    namespace="my_embeddings"
)
```

## Best Practices

1. **Dimension càng cao không phải lúc nào cũng tốt:**
   - 1536 dims (text-embedding-3-small) — đủ cho 90% use case
   - 3072 dims (text-embedding-3-large) — khi cần accuracy tối đa
2. **Query vs Document embedding** — Một số model dùng 2 function riêng
3. **Batch size** — Đừng embed quá nhiều cùng lúc (thường 100-500 documents/batch)
4. **Normalize vectors** — Nếu model chưa normalize, hãy normalize trước khi lưu
5. **Cache** — Luôn cache embeddings để tránh gọi API nhiều lần

## Trang Liên Quan

- [Vector Stores](vector-stores.md) — Lưu và tìm kiếm vector
- [Retrievers](retrievers.md) — Truy xuất documents
- [RAG](rag.md) — RAG architecture
