from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from summarizer import generate_summary

app = FastAPI()

# CORS for frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SummaryRequest(BaseModel):
    text: str
    bulletCount: int

@app.get("/")
def serve_ui():
    return FileResponse("frontend/index.html")

@app.post("/generate")
def generate(request: SummaryRequest):
    summary = generate_summary(request.text, request.bulletCount)
    return {"summary": summary}

@app.get("/ui")
def open_ui():
    return FileResponse("frontend/index.html")

