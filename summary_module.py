from gemini_client import generate_text
def summarize_text(text: str) -> str:
    return generate_text(
        "Summarize this educational text for revision. Use a heading, bullet points, and a short recap.\n\n" + text,
        "You are EduGenie's revision assistant. Preserve important facts and concepts."
    )
