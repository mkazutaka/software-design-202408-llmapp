from langchain.prompts.example_selector import (
    LengthBasedExampleSelector,
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

selector = LengthBasedExampleSelector(
    examples=examples,
    example_prompt=example_prompt,
    max_length=25,
    # デフォルトだとwordカウントになるのでstringカウントに変更している
    get_text_length=len,
)
print(selector.select_examples({}))
# => [{'sentence': 'これは素晴らしい!', 'answer': '1'}]
