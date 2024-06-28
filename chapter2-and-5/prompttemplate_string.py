from langchain_core.prompts import (
    PromptTemplate,
)

prompt_template = PromptTemplate.from_template(
    "与えた単語を{language}に変換してください"
)
result = prompt_template.invoke({"language": "日本語"})
print(result)
# => text='与えた単語を日本語に変換してください'
