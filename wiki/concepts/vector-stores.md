---
tags: [langchain, concept, core, rag]
created: 2026-06-25
updated: 2026-06-25
---

# Vector Stores — Lưu Trữ và Tìm Kiếm Vector

**Vector Stores** là database lưu trữ embeddings và hỗ trợ tìm kiếm vector (similarity search). Đây là thành phần trung tâm của RAG pipeline.

## Interface Cốt Lõi

```python
from langchain_core.vectorstores import VectorStore

# 1. Tạo từ documents
vectorstore = VectorStore.from_documents(
    documents=docs,          # list[Document]
    embedding=embeddings     # Embeddings model
)

# 2. Thêm documents
vectorstore.add_documents(more_docs)

# 3. Search
docs = vectorstore.similarity_search("query", k=4)
docs = vectorstore.similarity_search_with_score("query", k=4)
docs = vectorstore.max_marginal_relevance_search("query", k=4, fetch_k=20)

# 4. Convert to retriever
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 4})
```

## Các Vector Store Phổ Biến

### Chroma (Đơn giản, local)

```python
from langchain_chroma import Chroma

# Persistent
vectorstore = Chroma.from_documents(
    docs, embeddings,
    persist_directory="./chroma_db"
)

# Add more
vectorstore.add_documents(docs)
```

### FAISS (Fast, in-memory)

```python
from langchain_community.vectorstores import FAISS

vectorstore = FAISS.from_documents(docs, embeddings)

# Lưu & load
vectorstore.save_local("faiss_index")
vectorstore = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
```

### Pinecone (Managed, cloud)

```python
from langchain_pinecone import PineconeVectorStore

vectorstore = PineconeVectorStore(
    index_name="my-index",
    embedding=embeddings
)
```

### Qdrant (Self-hosted / Cloud)

```python
from langchain_qdrant import QdrantVectorStore

vectorstore = QdrantVectorStore.from_documents(
    docs, embeddings,
    url="http://localhost:6333",
    collection_name="my_collection"
)
```

### Weaviate

```python
from langchain_weaviate import WeaviateVectorStore
import weaviate

client = weaviate.Client("http://localhost:8080")
vectorstore = WeaviateVectorStore.from_documents(
    docs, embeddings, client=client, index_name="LangChain"
)
```

### PostgreSQL + pgvector

```python
from langchain_postgres import PGVector

vectorstore = PGVector.from_documents(
    docs, embeddings,
    connection="postgresql://user:pass@localhost:5432/db",
    collection_name="my_docs"
)
```

## So Sánh Vector Stores

| Store | Loại | Best For | Cloud | Free Tier |
|-------|------|----------|-------|-----------|
| Chroma | Local | Dev, prototyping | ❌ | ✅ |
| FAISS | Local | Speed, small datasets | ❌ | ✅ |
| Pinecone | Cloud | Production scaling | ✅ | ✅ (1 index) |
| Qdrant | Hybrid | Flexibility | ✅ | ✅ (1GB) |
| Weaviate | Hybrid | Full-text + vector search | ✅ | ✅ (sandbox) |
| PGVector | Local/Cloud | Already use Postgres | ✅ | ✅ |

## Advanced Search Modes

```python
# MMR — Đa dạng kết quả, tránh trùng lặp
vectorstore.max_marginal_relevance_search(query, k=4, fetch_k=20, lambda_mult=0.5)

# Similarity with score
docs_with_scores = vectorstore.similarity_search_with_score(query, k=4)
# Score càng thấp = càng giống (khoảng cách)

# Similarity by vector (không cần query text)
vectorstore.similarity_search_by_vector(query_vector, k=4)
```

## Best Practices

1. **Chọn store dựa trên scale:**
   - < 10K docs → Chroma / FAISS
   - 10K-1M docs → Qdrant / Weaviate
   - > 1M docs → Pinecone
2. **Metadata filtering** — Luôn thêm metadata filter để giảm search space
3. **Hybrid search** — Kết hợp full-text + vector (Qdrant, Weaviate)
4. **Index tuning** — Configure index type (HNSW, IVF) dựa trên recall/speed tradeoff

## Trang Liên Quan

- [Embeddings](embeddings.md) — Tạo vector từ text
- [Retrievers](retrievers.md) — Truy xuất từ vector store
- [RAG](rag.md) — RAG architecture
