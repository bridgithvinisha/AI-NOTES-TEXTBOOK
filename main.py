from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from summarizer import generate_summary

app = FastAPI()

# ---------------- Enable CORS ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allows frontend to call backend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- Serve frontend folder ----------
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")


# ---------- Route to open the UI ----------
@app.get("/")
def open_ui():
    return FileResponse("frontend/index.html")


# ---------- Request model for notes API ----------
class TextRequest(BaseModel):
    text: str
    num_sentences: int


# ---------- Notes Generate API ----------
@app.post("/generate-notes")
def generate_notes(req: TextRequest):
    summary = generate_summary(req.text, req.num_sentences)
    return {"notes": summary}


# ---------- Status API ----------
@app.get("/status")
def status():
    return {"message": "Backend Running Successfully!"}


