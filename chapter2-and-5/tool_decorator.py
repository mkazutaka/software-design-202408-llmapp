from langchain_core.tools import tool
from langchain.pydantic_v1 import (
    BaseModel,
    Field,
)


@tool
def multiply_1(a: int, b: int) -> int:
    """2つの数字を掛け算します"""
    return a * b


print(
    multiply_1.invoke({"a": 2, "b": 3})
)
print(multiply_1.name)
print(multiply_1.description)
print(multiply_1.args)
# => 6
# => multiply_1
# => 2つの数字を掛け算します
# => {'a': {'title': 'A', 'type': 'integer'}, 'b': {'title': 'B', 'type': 'integer'}}


class CalculatorInput(BaseModel):
    a: int = Field(description="数字1")
    b: int = Field(description="数字2")


@tool(
    "掛け算ツール2",
    args_schema=CalculatorInput,
    return_direct=True,
)
def multiply_2(a: int, b: int) -> int:
    """2つの数字を掛け算します"""
    return a * b


print(
    multiply_2.invoke({"a": 2, "b": 3})
)
print(multiply_2.name)
print(multiply_2.description)
print(multiply_2.args)
# => 6
# => 掛け算ツール2
# => 2つの数字を掛け算します
# => {'a': {'title': 'A', 'description': '数字1', 'type': 'integer'}, 'b': {'title': 'B', 'description': '数字2', 'type': 'integer'}}
