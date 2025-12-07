import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

def generate_notes(text, bullets=5):
    prompt = f"""
    Generate clear and concise textbook notes in bullet points.
    Number of bullet points: {bullets}
    Content: {text}

    Return bullet points only, no intro or summary lines.
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print("GENERATION ERROR:", e)
        return None



