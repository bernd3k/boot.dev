import os

from dotenv import load_dotenv
from google import genai

load_dotenv(verbose=True)
api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError(".env not found")


client = genai.Client(api_key=api_key)


def main():
    print("Hello from ai-agent!")
    client = genai.Client(api_key=api_key)
    response: genai.types.GenerateContentResponse = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
    )
    print(response.text)


if __name__ == "__main__":
    main()
