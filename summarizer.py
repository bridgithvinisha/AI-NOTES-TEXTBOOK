import google.generativeai as genai
import os

# Configure API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def generate_notes(paragraph: str, num_bullets: int = 5):
    """Generate bullet-point notes from a given paragraph."""
    prompt = f"""
    Summarize the following content into {num_bullets} clear bullet points:

    {paragraph}

    Format ONLY as bullet points without numbering.
    """

    response = model.generate_content(prompt)
    text = response.text.split("\n")

    # Cleanup
    bullets = [line.replace("-", "").strip() for line in text if line.strip()]
    bullets = bullets[:num_bullets]

    return "\n".join([f"• {b}" for b in bullets])


