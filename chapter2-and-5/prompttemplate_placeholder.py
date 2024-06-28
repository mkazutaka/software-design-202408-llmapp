from langchain_core.messages import (
    AIMessage,
    HumanMessage,
)
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
)

prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "与えた単語を{language}に変換してください",
        ),
        MessagesPlaceholder("messages"),
        # もしくは
        # ("placeholder", "{messages}"),
    ]
)

result = prompt_template.invoke(
    {
        "language": "日本語",
        "messages": [
            HumanMessage(content="Hello"),
            AIMessage(content="こんにちは"),
            HumanMessage(content="Good Morning"),
        ],
        # もしくは
        # "messages": [
        #    ("user", "Hello"),
        #    ("ai", "こんにちは"),
        #    ("user", "Good Morning"),
        # ]
    }
)
print(result)
# => messages=[SystemMessage(content='与えた単語を日本語に変換してください'), HumanMessage(content='Hello'), AIMessage(content='こんにちは'), HumanMessage(content='Good Morning')]
