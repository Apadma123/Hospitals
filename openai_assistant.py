import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

async def ask_openai(question: str):
    system_prompt = """
You are a helpful assistant for a hospital pricing app.
If the question is out of scope (e.g., weather), say: "I can only help with hospital pricing and quality information."
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message["content"]
