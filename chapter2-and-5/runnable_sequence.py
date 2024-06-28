from langchain_core.runnables import (
    RunnableLambda,
    RunnableSequence,
)


def add_one(x: int) -> int:
    return x + 1


runnable = RunnableLambda(add_one)
sequence_1 = runnable | runnable | runnable
sequence_2 = RunnableSequence(
    first=runnable,
    last=runnable,
    middle=[runnable],
)

print(sequence_1.invoke(0))
# => 3
print(sequence_2.invoke(0))
# => 3
print(sequence_1.batch([0, 1, 2]))
# => [3, 4, 5]
print(sequence_2.batch([0, 1, 2]))
# => [3, 4, 5]
