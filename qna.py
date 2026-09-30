from gemini_client import generate_text
def answer_question(question: str) -> str:
    return generate_text(
        f"Answer this student's question clearly and accurately:\n\n{question}",
        "You are EduGenie, a friendly educational tutor. Use simple language and useful examples."
    )
