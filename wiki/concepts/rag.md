---
tags: [langchain, concept, rag]
created: 2026-06-25
updated: 2026-06-25
---

# RAG — Retrieval-Augmented Generation

**RAG (Retrieval-Augmented Generation)** là kiến trúc kết hợp **truy xuất thông tin** (retrieval) với **sinh văn bản** (generation). Thay vì chỉ dùng kiến thức có sẵn trong model, RAG cho phép LLM truy xuất documents từ knowledge base và dùng chúng làm context để trả lời.

## Tại Sao RAG?

| Vấn Đề | Giải Pháp RAG |
|--------|---------------|
| Model không biết dữ liệu riêng | Inject documents vào context |
| Hallucination | Fact-check với retrieved documents |
| Kiến thức lỗi thời | Update knowledge base, không cần retrain |
| Chi phí fine-tuning cao | Zero training, chỉ cần indexing |

## RAG Pipeline Cổ Điển

```
                     Indexing Pipeline
                    ┌──────────────────┐
Documents ──► Load ──► Split ──► Embed ──► Store
                    └──────────────────┘

                     Retrieval Pipeline
                    ┌──────────────────┐
Query ──► Embed ──► Search ──► Retrieve ──► Context
                    └──────────────────┘

                     Generation Pipeline
                    ┌──────────────────────────┐
Context + Query ──► Prompt ──► LLM ──► Answer
                    └──────────────────────────┘
```

## Implementation với LangChain

### Basic RAG

```python
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. Indexing
raw_docs = loader.load()
splits = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200).split_documents(raw_docs)
vectorstore = Chroma.from_documents(splits, OpenAIEmbeddings())
retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

# 2. Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "Answer using ONLY the context below:\n\n{context}"),
    ("human", "{question}"),
])

# 3. Chain
def format_docs(docs):
    return "\n\n".join(d.page_content for d in docs)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | ChatOpenAI(model="gpt-4o")
    | StrOutputParser()
)

result = rag_chain.invoke("What is LangChain?")
```

### RAG với Citations

```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", """Answer based on context. Cite sources.

Context: {context}
Answer with citations like [Source: page X]"""),
    ("human", "{question}"),
])

def format_docs_with_metadata(docs):
    return "\n\n".join(
        f"[Source: {d.metadata.get('source', 'unknown')}] {d.page_content}"
        for d in docs
    )
```

### Advanced: RAG Fusion

Kết hợp nhiều retrieval strategies:

```python
from langchain.retrievers import EnsembleRetriever
from langchain_community.retrievers import BM25Retriever

# Vector search
vector_retriever = vectorstore.as_retriever()
# Keyword search (BM25)
bm25_retriever = BM25Retriever.from_documents(docs)

# Ensemble
ensemble_retriever = EnsembleRetriever(
    retrievers=[bm25_retriever, vector_retriever],
    weights=[0.3, 0.7]
)
```

## RAG Variants

### Corrective RAG
Khi retrieved documents không đủ chất lượng, tự động:
1. Retrieve → 2. Đánh giá relevance → 3. Nếu kém → web search fallback

### Self-RAG
LLM tự quyết định:
- Có cần retrieval không?
- Document nào liên quan?
- Câu trả lời có được support bởi document không?

### Agentic RAG
Agent có tools: retrieval, web search, calculation. Tự quyết định dùng tool nào.

## Evaluation Metrics

| Metric | Đo Gì | Cách Đo |
|--------|-------|---------|
| **Hit Rate** | % câu hỏi tìm được document đúng | So sánh retrieved vs ground truth |
| **MRR** | Rank của document đúng đầu tiên | Mean Reciprocal Rank |
| **NDCG** | Quality của ranking | Normalized Discounted Cumulative Gain |
| **Faithfulness** | Answer có đúng với context không | LLM-as-judge |
| **Answer Relevance** | Answer có trả lời câu hỏi không | LLM-as-judge |

## Best Practices

1. **Chunk strategy**:
   - 500-1000 tokens cho Q&A đơn giản
   - Parent-Child chunks cho context đầy đủ
   - Overlap 10-20% để tránh mất context biên

2. **Metadata filtering** — Giảm search space, tăng accuracy

3. **Hybrid search** — Kết hợp keyword (BM25) + vector search

4. **Re-ranking** — Dùng cross-encoder re-rank top-k trước khi đưa vào LLM

5. **Prompt engineering** — Instruction rõ "chỉ dùng context, nếu không có thì nói không biết"

## Trang Liên Quan

- [Retrievers](retrievers.md) — Truy xuất documents
- [Document Loaders](document-loaders.md) — Load dữ liệu
- [Text Splitters](text-splitters.md) — Chia nhỏ documents
- [Embeddings](embeddings.md) — Vector hóa text
- [Vector Stores](vector-stores.md) — Lưu trữ vector
- [Agent Architectures](agent-architectures.md) — Agentic RAG
