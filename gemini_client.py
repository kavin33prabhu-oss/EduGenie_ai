import time

from google import genai
from google.genai import types
from config import GEMINI_API_KEY, GEMINI_MODEL


client = genai.Client(api_key=GEMINI_API_KEY)


def generate_text(prompt: str, system_instruction: str = "") -> str:
    if not GEMINI_API_KEY:
        raise RuntimeError("GEMINI_API_KEY is missing. Add it to .env.")

    last_error = None

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction or None,
                    temperature=0.3,
                    max_output_tokens=2048,
                ),
            )

            return (response.text or "").strip()

        except Exception as error:
            last_error = error

            if "503" in str(error) or "UNAVAILABLE" in str(error):
                if attempt < 2:
                    time.sleep(2)
                    continue

            raise error

    raise last_error