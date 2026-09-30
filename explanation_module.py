from gemini_client import generate_text
def explain_topic(topic: str) -> str:
    return generate_text(
        f"Explain this topic for a beginner: {topic}\nUse: definition, key points, example, recap.",
        "You are EduGenie's concept explanation tutor. Make difficult ideas easy to understand."
    )
