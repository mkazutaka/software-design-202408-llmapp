from langchain_chroma import Chroma
from langchain_core.documents import (
    Document,
)
from langchain_openai import (
    OpenAIEmbeddings,
)

embeddings_model = OpenAIEmbeddings(model="text-embedding-3-small")

documents = [
    Document(
        page_content="今日の晩ごはんは、カレー？",
        metadata={"speaker": "son"},
    ),
    Document(
        page_content="今日の晩ごはんは、とんかつだよ",
        metadata={"speaker": "mother"},
    ),
    Document(
        page_content="カレーがよかったな",
        metadata={"speaker": "son"},
    ),
]

# ...省略

db = Chroma.from_documents(
    documents=documents,
    embedding=embeddings_model,
)
retriver = db.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 1},
)
result_documents = retriver.invoke("今日の晩ごはん")
print(result_documents[0])
# => page_content='今日の晩ごはんは、とんかつだよ' metadata={'speaker': 'mother'}
