from langchain_core.prompts import (
    ChatPromptTemplate,
)

temlate = ChatPromptTemplate.from_messages(
    messages=[
        (
            "system",
            "単語を{language}に変換して",
        ),
        ("user", "Hello"),
    ]
)
# もしくは
prompt_template = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(
            "与えた単語を{language}に変換してください"
        ),
        HumanMessage(content="Hello"),
    ]
)

result = temlate.invoke(
    {"language": "日本語"}
)
print(result)
# => messages=[SystemMessage(content='与えた単語を日本語に変換してください'), HumanMessage(content='Hello')]
