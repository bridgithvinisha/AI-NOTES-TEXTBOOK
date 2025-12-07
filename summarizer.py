import nltk
from nltk.tokenize import sent_tokenize

# Auto-download tokenizer if not available
nltk.download("punkt", quiet=True)

def generate_summary(text: str, num_sentences: int = 5):
    # Convert the text into individual sentences
    sentences = sent_tokenize(text)

    # Pick the first N sentences
    summary_sentences = sentences[:num_sentences]

    # Format into bullet points (each on a new line)
    summary = "\n".join([f"• {sentence.strip()}" for sentence in summary_sentences])

    return summary

