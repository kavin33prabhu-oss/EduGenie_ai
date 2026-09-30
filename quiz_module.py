import json
from gemini_client import generate_text

def generate_quiz(text: str) -> list:
    prompt = """Create exactly 3 multiple-choice questions from the material below.
Return ONLY valid JSON as an array. Each item must have:
question (string), options (array of exactly 4 strings),
correct_answer (one option string), explanation (string).

Material:
""" + text
    raw = generate_text(prompt, "You are EduGenie's quiz generator. Return only JSON.")
    data = json.loads(raw)
    if len(data) != 3:
        raise ValueError("Quiz must contain exactly 3 questions.")
    return data
