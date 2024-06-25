from langchain_core.runnables import (
    RunnableParallel,
    RunnablePassthrough,
)

runnable = RunnableParallel(
    origin=RunnablePassthrough(),
    add1=lambda x: x + 1,
)
print(runnable.invoke(1))
# => {'origin': 1, 'modified': 2}
