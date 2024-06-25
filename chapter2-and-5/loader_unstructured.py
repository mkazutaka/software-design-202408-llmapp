from langchain_community.document_loaders import (
    UnstructuredPDFLoader,
)

loader = UnstructuredPDFLoader(
    "data/layout-parser-paper.pdf",
    mode="elements",
    strategy="fast",
)

result = loader.load()
print(result[10])
# => page_content='Keywords: Document Image Analysis ·...省略
