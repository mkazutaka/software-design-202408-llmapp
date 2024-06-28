from langchain_chroma import Chroma
from langchain_core.documents import (
    Document,
)
from langchain_openai import (
    OpenAIEmbeddings,
)
from langchain.retrievers import (
    ContextualCompressionRetriever,
)
from langchain_openai import ChatOpenAI
from langchain_cohere.rerank import (
    CohereRerank,
)

model = ChatOpenAI(model="gpt-4o")
embaddings_model = OpenAIEmbeddings(model="text-embedding-3-small")


documents = [
    Document(
        page_content="今日の晩ごはんは、カレー？今日の晩ごはんは、とんかつだよ"
    ),
    Document(
        page_content="晩ごはんには、ハンバーガー。晩ごはんには、ハンバーガー"
    ),
    Document(page_content="今日の朝ごはんハンバーガーです。"),
    Document(page_content="明日の昼ご飯は、オムライスです。"),
    Document(page_content="明日の夜ご飯は、カレーハンバーグです。"),
]

db = Chroma.from_documents(
    documents=documents,
    embedding=embeddings_model,
)
retriever = db.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 4},
)
query = "今日の夜ご飯は？"
print(retriever.invoke(query)[0])
# => page_content='明日の夜ご飯は、カレーハンバーグです。'

compressor = CohereRerank(model="rerank-multilingual-v3.0")
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=retriever,
)
result = compression_retriever.invoke(query)
print(result[0])
# => page_content='今日の晩ごはんは、カレー？今日の晩ごはんは、とんかつだよ' metadata={'relevance_score': 0.9608049}
