from langchain_openai import (
    OpenAIEmbeddings,
)
from langchain_community.utils.math import (
    cosine_similarity,
)

embeddings_model = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

a = embeddings_model.embed_query(
    "Hello"
)
b = embeddings_model.embed_query(
    "こんにちは"
)
c = embeddings_model.embed_query(
    "こんばんは"
)
d = embeddings_model.embed_query(
    "明日のご飯はカレーです！"
)

print("次元数", len(a))
print(
    "aとbのコサイン類似度",
    cosine_similarity([a], [b]),
)
print(
    "aとcのコサイン類似度",
    cosine_similarity([a], [c]),
)
print(
    "aとdのコサイン類似度",
    cosine_similarity([a], [d]),
)
# => 次元数 1536
# => aとbのコサイン類似度 [[0.48905678]]
# => aとcのコサイン類似度 [[0.43020416]]
# => aとdのコサイン類似度 [[0.15197641]]
