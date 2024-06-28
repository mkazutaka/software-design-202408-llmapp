from langchain_core.runnables import (
    RunnableParallel,
)
from langchain_openai import ChatOpenAI
from langchain_core.prompts import (
    ChatPromptTemplate,
)
from langchain_core.output_parsers import (
    StrOutputParser,
)

parser = StrOutputParser()
model = ChatOpenAI(model="gpt-4o")

japanese_chain = (
    ChatPromptTemplate.from_template("日本語に翻訳: {query}") | model | parser
)
spanish_chain = (
    ChatPromptTemplate.from_template("スペイン語に翻訳: {query}")
    | model
    | parser
)
runnable = RunnableParallel(
    japanese=japanese_chain,
    spanish=spanish_chain,
)

output = {key: "" for key, _ in runnable.output_schema()}
for chunk in runnable.stream({"query": "It's a beautiful day today."}):
    for key in chunk:
        output[key] = output[key] + chunk[key]
        print(output)
# => {'japanese': '', 'spanish': ''}
# => {'japanese': '今日は', 'spanish': 'Hoy'}
# => ...省略
# => {'japanese': '今日は美しい日です。', 'spanish': 'Hoy es un día hermoso.'}
