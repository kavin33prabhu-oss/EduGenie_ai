# EduGenie

## VS Code setup

1. Extract the ZIP and open the `EduGenie` folder in VS Code.
2. Open **Terminal > New Terminal**.
3. Create a virtual environment:

Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Copy `.env.example` to `.env` and add your Gemini API key:
```env
GEMINI_API_KEY=YOUR_KEY
```

6. Run:
```bash
uvicorn main:app --reload
```

7. Open:
`http://127.0.0.1:8000`

Health check:
`http://127.0.0.1:8000/health`

## Features

- Q&A: `/qa`
- Explanation: `/explain`
- 3-question MCQ quiz: `/quiz`
- Summary: `/summarize`
- Learning path: `/learn/recommendations`
