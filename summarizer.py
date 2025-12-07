import google.generativeai as genai
import os

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")


def generate_notes(text, bullets):
    prompt = f"""
    Convert the following textbook paragraph into clear & concise {bullets} bullet-point notes.
    Text: {text}
    Bullet points:
    """

    response = model.generate_content(prompt)
    return response.text.strip()






