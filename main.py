from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from summarizer import generate_notes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/generate")
def generate(text: str, bullets: int = 5):
    result = generate_notes(text, bullets)
    if result is None:
        return {"error": "generation_failed"}
    return {"notes": result}

