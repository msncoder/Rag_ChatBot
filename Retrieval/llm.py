import os
from dotenv import load_dotenv
from google import genai

load_dotenv()


def generate_answer(prompt: str):

    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY not found in environment variables."
        )

    client = genai.Client(
        api_key=api_key
    )

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
     )

    return response.text