from langchain_core.output_parsers import (
    JsonOutputParser,
)
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_core.pydantic_v1 import (
    BaseModel,
    Field,
)
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o")


class TranslateResult(BaseModel):
    japanese: str = Field(description="日本語の結果")
    spanish: str = Field(description="スペイン語の結果")


parser = JsonOutputParser(pydantic_object=TranslateResult)

prompt_template = ChatPromptTemplate(
    messages=[
        SystemMessagePromptTemplate.from_template(
            "与えられた言語に翻訳してください\n{format_instructions}"
        ),
        HumanMessagePromptTemplate.from_template("{query}"),
    ],
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

prompt = prompt_template.invoke({"query", "hello"})
print(prompt)
# => messages=[SystemMessage(content='与えられた言語に翻訳してください\nThe output should be formatted as a JSON instance that conforms to the JSON schema below....省略

output = model.invoke(prompt)
result = parser.invoke(output)
print(result)
# => {'japanese': 'こんにちは', 'spanish': 'hola'}
