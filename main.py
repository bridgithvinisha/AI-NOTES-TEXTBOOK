from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from summarizer import generate_notes

app = FastAPI()

# Allow frontend calls
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "AI Notes API is running!"}

@app.get("/generate")
def generate(text: str, bullets: int):
    try:
        notes = generate_notes(text, bullets)
        return {"notes": notes}
    except Exception as e:
        return {"error": str(e)}





