---
tags: [langchain, concept, rag, retrievers]
created: 2026-06-25
updated: 2026-06-25
---

# Retrievers — Truy Xuất Thông Tin

**Retriever** là component chịu trách nhiệm truy xuất các documents liên quan đến câu hỏi. Đây là thành phần trung tâm của RAG (Retrieval-Augmented Generation).

## BaseRetriever Interface

```python
from langchain_core.retrievers import BaseRetriever
from langchain_core.documents import Document

class MyRetriever(BaseRetriever):
    def _get_relevant_documents(self, query: str) -> list[Document]:
        # Implement retrieval logic
        return [Document(page_content="result")]

    async def _aget_relevant_documents(self, query: str) -> list[Document]:
        # Async variant
        return self._get_relevant_documents(query)
```

## Các Loại Retriever

### 1. Vector Store Retriever (Phổ biến nhất)

```python
from langchain_community.vectorstores import Chroma

vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embeddings
)
retriever = vectorstore.as_retriever(
    search_type="similarity",  # similarity, mmr, similarity_score_threshold
    search_kwargs={"k": 4}     # số documents trả về
)

# Sử dụng
docs = retriever.invoke("What is LangChain?")
```

### 2. MultiQuery Retriever

Tự động sinh nhiều câu hỏi từ câu hỏi gốc, tìm kiếm từng câu, gộp kết quả.

```python
from langchain.retrievers.multi_query import MultiQueryRetriever

retriever = MultiQueryRetriever.from_llm(
    retriever=base_retriever,
    llm=model,
    include_original=True  # Giữ câu hỏi gốc
)
```

### 3. Contextual Compression Retriever

Nén documents — chỉ giữ phần liên quan đến câu hỏi.

```python
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor

compressor = LLMChainExtractor.from_llm(model)
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=base_retriever
)
```

### 4. Ensemble Retriever

Kết hợp nhiều retrievers với weights.

```python
from langchain.retrievers import EnsembleRetriever

retriever = EnsembleRetriever(
    retrievers=[bm25_retriever, vector_retriever],
    weights=[0.3, 0.7]  # BM25 30%, Vector 70%
)
```

### 5. Parent Document Retriever

Retrieve parent documents từ child chunks — giữ context đầy đủ.

```python
from langchain.retrievers import ParentDocumentRetriever

retriever = ParentDocumentRetriever(
    vectorstore=vectorstore,
    docstore=InMemoryStore(),
    child_splitter=RecursiveCharacterTextSplitter(chunk_size=200),
    parent_splitter=RecursiveCharacterTextSplitter(chunk_size=2000)
)
```

### 6. Time-Weighted Retriever

Ưu tiên documents mới hơn hoặc được truy cập nhiều hơn.

```python
from langchain.retrievers import TimeWeightedVectorStoreRetriever

retriever = TimeWeightedVectorStoreRetriever(
    vectorstore=vectorstore,
    decay_rate=0.01  # Càng thấp, càng quên nhanh
)
```

## Search Types cho VectorStore

```python
# similarity — KNN truyền thống
retriever = vs.as_retriever(search_type="similarity", search_kwargs={"k": 4})

# mmr — Maximum Marginal Relevance (đa dạng kết quả)
retriever = vs.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 4, "fetch_k": 20, "lambda_mult": 0.5}
)

# similarity_score_threshold — Chỉ lấy kết quả > threshold
retriever = vs.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"score_threshold": 0.7}
)
```

## RAG Pipeline Điển Hình

```python
# 1. Load -> Split -> Embed -> Store
loader = TextLoader("doc.txt")
docs = loader.load()
splits = text_splitter.split_documents(docs)
vectorstore = Chroma.from_documents(splits, embeddings)

# 2. Retrieve
retriever = vectorstore.as_retriever()

# 3. Format + Generate
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | model
    | parser
)
```

## Best Practices

1. **Kết hợp nhiều retrievers** — Dùng ensemble retriever cho kết quả tốt nhất
2. **ParentDocumentRetriever** cho context đầy đủ — Chunk nhỏ để search, trả về document lớn
3. **MultiQuery** khi câu hỏi mơ hồ — Tự động paraphrase
4. **Compression** khi context window hẹp — Chỉ giữ phần liên quan
5. **Luôn MMR** nếu cần đa dạng — Tránh kết quả trùng lặp

## Trang Liên Quan

- [Document Loaders](document-loaders.md) — Load documents từ nhiều nguồn
- [Text Splitters](text-splitters.md) — Chia nhỏ documents
- [Embeddings](embeddings.md) — Chuyển text thành vector
- [Vector Stores](vector-stores.md) — Lưu trữ và tìm kiếm vector
- [RAG](rag.md) — RAG architecture
