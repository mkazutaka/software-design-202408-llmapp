from langchain_openai import ChatOpenAI
from langchain_core.prompts import (
    ChatPromptTemplate,
)
from langchain.chains import LLMChain

model = ChatOpenAI(
    model="gpt-3.5-turbo"
)
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "与えた単語を{language}に変換してください",
        ),
        ("user", "hi"),
    ]
)

chain = LLMChain(
    llm=model, prompt=prompt
)
result = chain.run(
    {
        "language": "日本語",
    }
)
print(result)  # => こんにちは
