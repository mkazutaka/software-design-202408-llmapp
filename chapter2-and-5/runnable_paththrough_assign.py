from langchain_openai import ChatOpenAI
from langchain_core.runnables import (
    RunnablePassthrough,
)
from langchain_core.output_parsers import (
    StrOutputParser,
)

model = ChatOpenAI(model="gpt-4o")
runnable = {
    "llm": model | StrOutputParser()
} | RunnablePassthrough.assign(
    length=lambda input: len(
        input["llm"]
    )
)
print(runnable.invoke("こんにちわ"))
# => {'llm': 'こんにちは！今日はどんなことをお手伝いしましょうか？', 'length': 26}
