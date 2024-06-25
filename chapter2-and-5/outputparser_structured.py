from langchain.output_parsers import (
    ResponseSchema,
    StructuredOutputParser,
)
from langchain_core.output_parsers import (
    StrOutputParser,
)
from langchain_core.prompts import (
    PromptTemplate,
)
from langchain_openai import ChatOpenAI

response_schemas = [
    ResponseSchema(
        name="answer",
        description="answer to the user's question",
    ),
    ResponseSchema(
        name="source",
        description="source used to answer the user's question, should be a website.",
    ),
]
output_parser = StructuredOutputParser.from_response_schemas(
    response_schemas
)

print(
    output_parser.get_format_instructions()
)
