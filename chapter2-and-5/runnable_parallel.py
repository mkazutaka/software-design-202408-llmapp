from langchain_core.runnables import (
    RunnableLambda,
    RunnableParallel,
)


def add_one(x: int) -> int:
    return x + 1


runnable = RunnableLambda(add_one)
sequence_1 = runnable | {
    "two": runnable,
    "three": runnable | runnable,
}
sequence_2 = runnable | RunnableParallel(
    two=runnable,
    three=runnable | runnable,
)

print(sequence_1.invoke(0))
# => {'two': 2, 'three': 3}
print(sequence_2.invoke(0))
# => {'two': 2, 'three': 3}
