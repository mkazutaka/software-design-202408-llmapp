from langchain_core.messages import (
    AIMessage,
)
from langchain_core.output_parsers import (
    StrOutputParser,
)

parser = StrOutputParser()
message = AIMessage(
    content="こんにちは！元気ですか？何かお手伝いできることはありますか？"
)
result = parser.invoke(message)
print(result)
# => こんにちは！元気ですか？何かお手伝いできることはありますか？
