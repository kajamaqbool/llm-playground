import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("Please set the OPENROUTER_API_KEY environment variable.")

client = OpenAI(
    api_key=api_key,
    base_url = "https://openrouter.ai/api/v1",
)

prompt = "Suggest a name for coffee shop."

temperatures = [0, 0.3, 0.7, 1.0, 1.5]

for temp in temperatures:
    print(f"\n--- Temperature: {temp} ---")
    for i in range(3):
        response = client.chat.completions.create(
            model = "openai/gpt-5.4-mini",
            messages = [
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            temperature = temp,
            max_completion_tokens = 50
        )
        print(f" Run {i + 1}: {response.choices[0].message.content}")