---
tags: [langchain, concept, rag, document-loaders]
created: 2026-06-25
updated: 2026-06-25
---

# Document Loaders — Load Dữ Liệu Từ Mọi Nguồn

**Document Loaders** là component cho phép load dữ liệu từ 100+ định dạng và nguồn khác nhau. Mỗi loader chuyển đổi dữ liệu nguồn thành `Document(page_content, metadata)`.

## Document Structure

```python
from langchain_core.documents import Document

doc = Document(
    page_content="This is the text content...",
    metadata={
        "source": "file.pdf",
        "page": 1,
        "author": "John Doe"
    }
)
```

## Các Loader Phổ Biến

### Văn Bản & Code
```python
from langchain_community.document_loaders import (
    TextLoader,       # .txt files
    CSVLoader,        # .csv files
    UnstructuredFileLoader,  # General purpose
    PythonLoader,     # .py files
    JSONLoader,       # .json files
)
```

### PDF
```python
from langchain_community.document_loaders import (
    PyPDFLoader,      # PDF text extraction
    PyMuPDFLoader,    # Fast PDF (using PyMuPDF)
    PDFPlumberLoader, # PDF with tables
    UnstructuredPDFLoader,  # Complex PDFs
)
```

### Web
```python
from langchain_community.document_loaders import (
    WebBaseLoader,        # HTML pages
    SeleniumURLLoader,    # Dynamic JS pages
    AsyncHtmlLoader,      # Async HTML loading
    BSHTMLLoader,         # BeautifulSoup HTML
    RecursiveUrlLoader,   # Crawl multiple pages
)
```

### Databases
```python
from langchain_community.document_loaders import (
    TextLoader,           # SQL databases
    MongoDBLoader,        # MongoDB
)
```

### Multimedia & Office
```python
from langchain_community.document_loaders import (
    UnstructuredWordLoader,   # .docx
    UnstructuredPowerPointLoader,  # .pptx
    UnstructuredExcelLoader,  # .xlsx
    UnstructuredImageLoader,  # Images (OCR)
    UnstructuredEmailLoader,  # .eml, .msg
)
```

## Lazy Loading

Với file lớn, dùng lazy loading để không load hết vào memory:

```python
loader = PyPDFLoader("large.pdf")
pages = []  # Không giữ toàn bộ

for page in loader.lazy_load():
    process_page(page)

# Hoặc lazy với alazy
async for page in loader.alazy_load():
    await process_page(page)
```

## Custom Loader

```python
from langchain_core.document_loaders import BaseLoader
from langchain_core.documents import Document

class MyCustomLoader(BaseLoader):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def lazy_load(self):
        with open(self.file_path, "r") as f:
            for line in f:
                yield Document(
                    page_content=line.strip(),
                    metadata={"source": self.file_path}
                )
```

## Multi-Modal Loaders

```python
# Load images + text từ PDF
from langchain_community.document_loaders.parsers import (
    LLMSingleFileParser,
    Blob,
)

# Load với OCR
from langchain_community.document_loaders import UnstructuredImageLoader
loader = UnstructuredImageLoader("scanned_doc.png",
    strategy="ocr_only"  # Hoặc "auto", "fast"
)
```

## Trang Liên Quan

- [Text Splitters](text-splitters.md) — Chia nhỏ documents sau khi load
- [Retrievers](retrievers.md) — Truy xuất documents
- [RAG](rag.md) — RAG architecture
