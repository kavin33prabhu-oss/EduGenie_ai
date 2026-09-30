from pathlib import Path
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from config import DEBUG, MAX_INPUT_CHARS
from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations

BASE_DIR = Path(__file__).resolve().parent
app = FastAPI(title="EduGenie", version="1.0.0", debug=DEBUG)
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

class TextRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=MAX_INPUT_CHARS)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
   return templates.TemplateResponse(request, "index.html")

@app.get("/health")
def health():
    return {"status": "ok", "service": "EduGenie"}

def clean(value: str) -> str:
    value = value.strip()
    if not value:
        raise HTTPException(400, "Please enter some text.")
    return value

@app.post("/qa")
def qa(payload: TextRequest):
    try: return {"result": answer_question(clean(payload.text))}
    except Exception as e: raise HTTPException(500, str(e))

@app.post("/explain")
def explain(payload: TextRequest):
    try: return {"result": explain_topic(clean(payload.text))}
    except Exception as e: raise HTTPException(500, str(e))

@app.post("/quiz")
def quiz(payload: TextRequest):
    try: return {"result": generate_quiz(clean(payload.text))}
    except Exception as e: raise HTTPException(500, str(e))

@app.post("/summarize")
def summarize(payload: TextRequest):
    try: return {"result": summarize_text(clean(payload.text))}
    except Exception as e: raise HTTPException(500, str(e))

@app.post("/learn/recommendations")
def recommendations(payload: TextRequest):
    try: return {"result": get_learning_recommendations(clean(payload.text))}
    except Exception as e: raise HTTPException(500, str(e))
