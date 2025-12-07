# models.py
from pydantic import BaseModel, Field

class NotesRequest(BaseModel):
    text: str = Field(
        ...,
        description="Long textbook text from which notes will be generated"
    )
    num_sentences: int = Field(
        8,
        description="Approximate number of note points to generate",
        ge=3,
        le=30
    )
