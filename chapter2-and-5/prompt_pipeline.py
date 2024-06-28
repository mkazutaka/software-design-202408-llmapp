from langchain_core.prompts.pipeline import (
    PipelinePromptTemplate,
)
from langchain_core.prompts.prompt import (
    PromptTemplate,
)

final_template = """{template1} {template2}"""
final_prompt = PromptTemplate.from_template(final_template)

first_template = """あなたは、{role}です。"""
first_prompt = PromptTemplate.from_template(first_template)

second_template = """{role}は、{description}。"""
second_prompt = PromptTemplate.from_template(second_template)

pipeline_prompt = PipelinePromptTemplate(
    final_prompt=final_prompt,
    pipeline_prompts=[
        ("template1", first_prompt),
        (
            "template2",
            second_prompt,
        ),
    ],
)
print(pipeline_prompt.input_variables)
# => ['description', 'role']

print(
    pipeline_prompt.invoke(
        {
            "role": "シェフ",
            "description": "美味しい料理を作ります",
        }
    )
)
# => text='あなたは、シェフです。 シェフは、美味しい料理を作ります。'
