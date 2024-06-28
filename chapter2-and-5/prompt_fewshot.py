from langchain_core.prompts import (
    FewShotPromptTemplate,
)
from langchain_core.prompts import (
    PromptTemplate,
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
example_prompt = PromptTemplate.from_template(
    """
Text: {sentence}
Answer: {answer}
""".strip()
)
print(example_prompt.invoke(examples[0]))
# => text='Text: これは素晴らしい!\nAnswer: 1'

prefix = "以下のTextから0か1かを判定してください"
suffix = "Text: {input}\nAnswer: "
prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="以下のTextから0か1かを判定してください",
    suffix="Text: {input}\nAnswer: ",
    input_variables=["input"],
    example_separator="\n",
)
print(prompt.invoke({"input": "なんてひどいショーだ！"}).text)
# => 以下のTextから0か1かを判定してください。回答のみを答えてください。
# => Text: これは素晴らしい!
# => Answer: 1
# => Text: これは悪いことだ！
# => Answer: 0
# => Text: なんてひどいショーなんだ！
# => Answer:
