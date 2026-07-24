import os
from pathlib import Path

from dotenv import load_dotenv

try:
    from .utils import load_csv_dataframe
except ImportError:  # pragma: no cover - support script-style execution
    from backend.app.utils import load_csv_dataframe

try:
    from langchain_groq import ChatGroq
except ImportError:  # pragma: no cover - exercised in minimal environments
    ChatGroq = None

BACKEND_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BACKEND_DIR / ".env")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    GROQ_API_KEY = ""

os.environ["GROQ_API_KEY"] = GROQ_API_KEY

GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0"))

CAREER_DOMAINS_CSV = BACKEND_DIR / "career_domains.csv"
PROJECTS_CSV = BACKEND_DIR / "projects.csv"

career_df = load_csv_dataframe(CAREER_DOMAINS_CSV)
projects_df = load_csv_dataframe(PROJECTS_CSV)

if ChatGroq is None or not GROQ_API_KEY:
    llm = None
else:
    llm = ChatGroq(
        model=GROQ_MODEL,
        temperature=LLM_TEMPERATURE,
        api_key=GROQ_API_KEY,
    )
