import google.generativeai as genai
import os

# Load Gemini API key from Render environment variable
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Gemini model selection
model = genai.GenerativeModel("gemini-pro")


def generate_notes(text, bullets=5):
    try:
        if not text or text.strip() == "":
            return None

        prompt = (
            f"Generate {bullets} clear, structured academic bullet points based on the following textbook paragraph:\n\n"
            f"{text}\n\n"
            "Return ONLY bullet points without title or explanation."
        )

        response = model.generate_content(prompt)

        # ---- Extract response safely ----
        # 1️⃣ If standard attribute exists
        if hasattr(response, "text") and response.text:
            return response.text.strip()

        # 2️⃣ Some responses structure text differently
        if hasattr(response, "candidates") and response.candidates:
            parts = response.candidates[0].content.parts
            if parts and hasattr(parts[0], "text"):
                return parts[0].text.strip()

        # If nothing returned (rare case)
        return None

    except Exception as e:
        print("GENERATION ERROR:", e)
        return None





