from gemini_client import generate_text
def get_learning_recommendations(topic: str) -> str:
    return generate_text(
        f"""Create a beginner-to-advanced learning path for {topic}.
For each stage include concepts, practical activity, approximate study time,
and useful resource types. Finish with a weekly revision plan.""",
        "You are EduGenie's learning-path mentor. Make the plan practical and step-by-step."
    )
