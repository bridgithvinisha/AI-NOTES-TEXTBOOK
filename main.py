from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from summarizer import generate_summary
from fastapi.responses import FileResponse







app = FastAPI()

# ---------------- Enable CORS ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],     # allows frontend to call backend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 
# ---------------- Request Model ----------------
class NotesRequest(BaseModel):
    text: str
    num_sentences: int

# ---------------- Routes ----------------
@app.get("/")
def root():
    return {"message": "AI Notes Generator from Textbooks is running!"}

@app.post("/generate-notes")
def generate_notes(req: NotesRequest):
    summary = generate_summary(req.text, req.num_sentences)
    return {"notes": summary}

@app.get("/ui")
def open_ui():
    return FileResponse("frontend/index.html")

