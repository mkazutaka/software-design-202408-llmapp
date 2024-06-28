from langchain_community.document_loaders import (
    PyPDFLoader,
)

loader = PyPDFLoader("data/layout-parser-paper.pdf")
result = loader.load()
print(result[0])
