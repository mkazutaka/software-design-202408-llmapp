from langchain_core.runnables import (
    RunnablePassthrough,
)
from langchain_core.prompts import (
    ChatPromptTemplate,
)
from langchain_chroma import Chroma
from langchain_core.documents import (
    Document,
)
from langchain_openai import (
    OpenAIEmbeddings,
)
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import (
    StrOutputParser,
)

model = ChatOpenAI(
    model="gpt-3.5-turbo"
)
embeddings_model = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

documents = [
    Document(
        page_content="今日の晩ごはんは、カレー？"
    ),
    Document(
        page_content="今日の晩ごはんは、とんかつだよ"
    ),
    Document(
        page_content="カレーがよかったな"
    ),
]
db = Chroma.from_documents(
    documents=documents,
    embedding=embeddings_model,
)
retriever = db.as_retriever(
    search_kwargs={"k": 1}
)
prompt = (
    ChatPromptTemplate.from_template("""
以下の情報を下に回答してください:
{context}
---
質問: {question}
""")
)
retrieval_chain = (
    {
        "context": retriever,
        "question": RunnablePassthrough(),
    }
    | prompt
    | model
    | StrOutputParser()
)

print(
    retrieval_chain.invoke(
        "今日の晩ごはんは何？"
    )
)
# => 回答: 今日の晩ごはんは、とんかつです。
