from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from summarizer import generate_notes

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class NotesRequest(BaseModel):
    text: str
    bullets: int

@app.get("/")
def home():
    return {"message": "AI Notes API is running!"}

@app.post("/generate")
def generate(request: NotesRequest):
    notes = generate_notes(request.text, request.bullets)
    return {"notes": notes}



