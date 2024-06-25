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
from langchain.retrievers.document_compressors import (
    LLMChainExtractor,
)
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o")
embeddings_model = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

documents = [
    Document(
        page_content="冷凍のカレーがあるよ。今日の晩ごはんは、とんかつだよ。最近、天気がずっといいね。洗濯物がよく乾くわ。カレーがよかったな。最近、天気がずっといいね。洗濯物がよく乾くわ。来週は友達と遊びに行く予定があるんだ。楽しみだな。"
    ),
]

db = Chroma.from_documents(
    documents=documents,
    embedding=embeddings_model,
)
retriever = db.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 1},
)
print(
    retriever.invoke("今日の晩ごはん")
)
# => [Document(page_content='冷凍のカレーがあるよ。今日の晩ごはんは、とんかつだよ。最近、天気がずっといいね。洗濯物がよく乾くわ。カレーがよかったな。最近、天 気がずっといいね。洗濯物がよく乾くわ。来週は友達と遊びに行く予定があるんだ。楽しみだな。')]

compressor = LLMChainExtractor.from_llm(
    model
)
compression_retriever = (
    ContextualCompressionRetriever(
        base_compressor=compressor,
        base_retriever=retriever,
    )
)

result = compression_retriever.invoke(
    "今日の晩ごはん"
)
print(result)
# => [Document(page_content='今日の晩ごはんは、とんかつだよ。')]
