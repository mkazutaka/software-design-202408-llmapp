from langchain_chroma import Chroma
from langchain_core.example_selectors import (
    SemanticSimilarityExampleSelector,
)
from langchain_openai import (
    OpenAIEmbeddings,
)

examples = [
    {
        "sentence": "これは素晴らしい!",
        "answer": "1",
    },
    {
        "sentence": "これは悪いことだ！",
        "answer": "0",
    },
]
embeddings_model = OpenAIEmbeddings(model="text-embedding-3-small")

selector = SemanticSimilarityExampleSelector.from_examples(
    examples=examples,
    embeddings=embeddings_model,
    vectorstore_cls=Chroma,
    k=1,
)
selected_examples = selector.select_examples({"question": "素晴らしい"})
print(selected_examples)
# => [{'answer': '1', 'sentence': 'これは素晴らしい!'}]
