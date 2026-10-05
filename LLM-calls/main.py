import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("Set the OPENROUTER_API_KEY environment variable in your .env file.")

client = OpenAI(
    api_key=api_key,
    base_url = "https://openrouter.ai/api/v1",
)

response = client.chat.completions.create(
    model = "openrouter/free",
    messages = [
        {
            "role": "system",
            "content": "You are a senior software engineer. Give concise, practical answers.",
        },
        {
            "role": "user",
            "content": "What are the three most important things to know about database indexing?",
        },
    ],
    max_completion_tokens = 300
)

answer = response
print(answer)

if response.usage:
    print(
        f"\nToken used - Input: {response.usage.prompt_tokens}, "
        f"Output: {response.usage.completion_tokens}, "
        f"Total: {response.usage.total_tokens}"
    )