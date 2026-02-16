import os
from dotenv import load_dotenv
from pathlib import Path

# load .env if it exists (optional now)
BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / ".env"

if env_path.exists():
    load_dotenv(dotenv_path=env_path)

# optional — used only if you later switch back to cloud models
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", None)
