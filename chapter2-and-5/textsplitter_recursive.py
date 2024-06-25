from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
)

TEXT = """12345 67890abcdefghij"""

text_splitter = (
    RecursiveCharacterTextSplitter(
        chunk_size=5,
        chunk_overlap=2,
        separators=[" ", ""],
    )
)
splitted = text_splitter.split_text(
    TEXT
)
for i in range(len(splitted)):
    print(i, splitted[i])

# => 0 12345
# => 1 6789
# => 2 890ab
# => 3 abcde
# => 4 defgh
# => 5 ghij
