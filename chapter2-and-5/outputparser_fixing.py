from langchain_core.output_parsers import (
    JsonOutputParser,
)
from langchain_core.pydantic_v1 import (
    BaseModel,
    Field,
)
from langchain_openai import ChatOpenAI
from langchain.output_parsers.fix import (
    OutputFixingParser,
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
fixing_parser = OutputFixingParser.from_llm(parser=parser, llm=model)
print(fixing_parser.invoke(missing_json))
# => {'japanese': 'こんにちは', 'spanish': 'hola'}
