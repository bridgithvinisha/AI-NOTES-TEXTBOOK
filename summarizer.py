import os
import requests

HF_API_KEY = os.getenv("HF_API_KEY")

MODEL = "mistralai/Mixtral-8x7B-Instruct-v0.1"

API_URL = f"https://api-inference.huggingface.co/models/{MODEL}"
HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}


def generate_notes(text, bullet_count):
    prompt = f"""
    Summarize the following content into exactly {bullet_count} clear bullet points formatted with "•":
    Content:
    {text}
    """

    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code != 200:
        raise Exception(f"HF API Error: {response.text}")

    result = response.json()[0]["generated_text"]
    return result







