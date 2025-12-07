from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.responses import FileResponse
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# --- CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Gemini Key ---
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

# --- Request model ---
class NotesRequest(BaseModel):
    text: str
    num_points: int

# --- Root ---
@app.get("/")
def home():
    return {"message": "AI Notes Generator from Textbooks is running!"}

# --- Serve frontend UI ---
@app.get("/ui")
def serve_ui():
    return FileResponse("frontend/index.html")

# Static files (CSS/JS)
app.mount("/static", StaticFiles(directory="frontend"), name="static")


# --- Notes generation endpoint ---
@app.post("/generate")
def generate_notes(data: NotesRequest):
    """
    Generates AI bullet notes from paragraph using Gemini model.
    """
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = (
            f"Generate exactly {data.num_points} clear and short bullet points "
            f"from the following paragraph:\n\n{data.text}"
        )

        response = model.generate_content(prompt)
        notes = [line.strip("-• ") for line in response.text.split("\n") if line.strip()]

        return {"notes": notes[:data.num_points]}
    except Exception as e:
        return {"error": str(e)}




