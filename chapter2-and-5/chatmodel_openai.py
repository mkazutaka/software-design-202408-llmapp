from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="gpt-3.5-turbo"
)
messages = [("user", "こんにちは")]
result = model.invoke(messages)
print(result)
# => content='こんにちは！元気ですか？何かお手伝いできることはありますか？' response_metadata={'token_usage': {'completion_tokens': 24, ...省略
