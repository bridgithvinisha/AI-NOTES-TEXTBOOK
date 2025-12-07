from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from summarizer import generate_notes

app = FastAPI()

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "AI Notes API is running!"}

@app.get("/generate")
def generate(text: str, bullets: int = 5):
    # Call Gemini model
    notes = generate_notes(text, bullets)
    
    # If failure
    if not notes:
        return {"error": "generation_failed"}
    
    # Send to frontend
    return {"notes": notes}


