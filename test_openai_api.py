from openai import OpenAI

client = OpenAI(api_key=OPENAI_API_KEY)
from configs.config import OPENAI_API_KEY

def test_openai_api():
    try:
        response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is the capital of Canada?"}
        ])
        print("API Response:", response.choices[0].message.content.strip())
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    test_openai_api()