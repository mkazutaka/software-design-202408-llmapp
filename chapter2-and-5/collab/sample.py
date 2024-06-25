from openai import OpenAI
from google.colab import (
    userdata,
)

# OpenAI APIから取得し、
# Google Collabのシークレットに保存
api_key = userdata.get("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)
result = client.chat.completions.create(
    model="gpt-4o-2024-05-13",
    messages=[
        {
            "role": "user",
            "content": "技術評論社について教えて",
        }
    ],
)
print(result.choices[0].message.content)

############################

import anthropic
from google.colab import userdata

# Anthropic Consoleから取得し、Google Collabのシークレットに保存
api_key = userdata.get(
    "ANTHROPIC_API_KEY"
)
client = anthropic.Anthropic(
    api_key=api_key
)
result = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=4096,
    messages=[
        {
            "role": "user",
            "content": "技術評論社について教えて",
        }
    ],
)
print(result.content[0].text)

############################
import google.generativeai as genai
from google.colab import userdata

# Google AI StudioからAPIキーを取得し、Colabのシークレットに保存
api_key = userdata.get("GOOGLE_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel(
    "gemini-1.5-pro-latest"
)
response = model.generate_content(
    "技術評論社について教えて"
)
print(response.text)
