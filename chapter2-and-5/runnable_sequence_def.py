from langchain_core.runnables import (
    RunnableLambda,
)


def add_one(x: int) -> int:
    return x + 1


runnable = RunnableLambda(add_one)
# add_oneはRunnableSequenceではないが実行可能
sequence_1 = runnable | add_one

print(sequence_1.invoke(0))
# => 2
