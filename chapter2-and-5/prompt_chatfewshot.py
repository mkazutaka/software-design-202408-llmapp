from langchain_core.prompts import (
    ChatPromptTemplate,
    FewShotChatMessagePromptTemplate,
)

examples = [
    {
        "sentence": "これはすばらしい!",
        "answer": "1",
    },
    {
        "sentence": "これは悪いことだ！",
        "answer": "0",
    },
]
example_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "human",
            "Text: {sentence}\nAnswer:",
        ),
        ("ai", "{answer}"),
    ]
)
few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=examples,
)
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "以下のTextから0か1かを判定してください。",
        ),
        few_shot_prompt,
        (
            "human",
            "Text: {input}\nAnswer: ",
        ),
    ]
)
print(prompt.invoke({"input": "なんてひどいショーなんだ！"}).to_messages())
# => [SystemMessage(content='以下のTextから0か1かを判定してください。'),
#     HumanMessage(content='Text: これはすばらしい!\nAnswer:'),
#     AIMessage(content='1'),
#     HumanMessage(content='Text: これは悪いことだ！\nAnswer:'),
#     AIMessage(content='0'),
#     HumanMessage(content='Text: なんてひどいショーなんだ！\nAnswer: ')]
