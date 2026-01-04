from openai import OpenAI
import json
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def generate_nickname(input_data: dict) -> dict:
    prompt = f"""
You are a nickname recommendation API.

Return ONLY valid JSON.
Do not include explanations or markdown.

JSON schema:
{{
  "categories": [
    {{
      "theme": "string",
      "nicknames": [
        {{
          "name": "string",
          "description": "string"
        }}
      ]
    }}
  ]
}}

User input:
Name: {input_data['name']}
Age: {input_data['age']}
Gender: {input_data['gender']}
Vibe: {input_data['vibe']}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    return json.loads(response.choices[0].message.content)
