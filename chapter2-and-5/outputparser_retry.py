from langchain_core.output_parsers import (
    JsonOutputParser,
)
from langchain_core.pydantic_v1 import (
    BaseModel,
    Field,
)
from langchain_openai import ChatOpenAI
from langchain.output_parsers.retry import (
    RetryWithErrorOutputParser,
)
from langchain_core.prompts import (
    PromptTemplate,
)

missing_json = '{"japanese": "こんにちは"\n "spanish": "hola"}'


class TranslateResult(BaseModel):
    japanese: str = Field(description="日本語の結果")
    spanish: str = Field(description="スペイン語の結果")


parser = JsonOutputParser(pydantic_object=TranslateResult)
try:
    print(parser.invoke(missing_json))
    # => Error: json.decoder.JSONDecodeError: Expecting ',' delimiter: line 2 column 2 (char 22)
except:
    pass

model = ChatOpenAI(model="gpt-3.5-turbo")
retry_parser = RetryWithErrorOutputParser.from_llm(parser=parser, llm=model)

prompt_template = PromptTemplate.from_template(
    "与えられた言語に翻訳してください\n{format_instructions}\n{query}"
)
prompt = prompt_template.invoke(
    {
        "format_instructions": parser.get_format_instructions(),
        "query": "こんにちは",
    }
)

print(retry_parser.parse_with_prompt(missing_json, prompt))
# => {'japanese': 'こんにちは', 'spanish': 'hola'}
