from langchain_chroma import Chroma
from langchain_core.documents import (
    Document,
)
from langchain_openai import (
    OpenAIEmbeddings,
)

from langchain_core.prompts import (
    FewShotPromptTemplate,
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

db = Chroma.from_documents(
    documents=documents,
    embedding=embeddings_model,
)
result_documents = db.similarity_search(query="今日の晩ごはん", k=1)
print(result_documents[0])
# => page_content='今日の晩ごはんは、とんかつだよ' metadata={'speaker': 'mother'}
