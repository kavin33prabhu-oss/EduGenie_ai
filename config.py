import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
MAX_INPUT_CHARS = int(os.getenv("MAX_INPUT_CHARS", "12000"))
DEBUG = os.getenv("DEBUG", "true").lower() == "true"
