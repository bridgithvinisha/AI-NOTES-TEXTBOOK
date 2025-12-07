






from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from summarizer import generate_notes
import uvicorn
import os

app = FastAPI()

# Allow frontend JS to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve frontend
@app.get("/")
def index():
    return FileResponse("frontend/index.html")

@app.get("/style.css")
def css():
    return FileResponse("frontend/style.css")

@app.get("/script.js")
def js():
    return FileResponse("frontend/script.js")


# API endpoint
@app.post("/generate")
async def generate(data: dict):
    paragraph = data.get("paragraph", "")
    num_bullets = int(data.get("num_bullets", 5))
    notes = generate_notes(paragraph, num_bullets)
    return {"notes": notes}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT", 10000)))
