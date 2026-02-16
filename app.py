import threading
import subprocess
import time
import webbrowser
from pathlib import Path
import uvicorn

# -----------------------------
# Prevent double browser launch
# -----------------------------
flag = Path(".browser_opened")
if flag.exists():
    flag.unlink()


# -----------------------------
# Run FastAPI backend
# -----------------------------
def run_backend():
    uvicorn.run(
        "application.main:app",
        host="127.0.0.1",
        port=8000,
        reload=False
    )


# -----------------------------
# Run Streamlit frontend
# -----------------------------
def run_frontend():
    time.sleep(3)  # wait backend ready
    subprocess.run(
        [
            "streamlit",
            "run",
            "dashboard/frontend.py",
            "--server.port",
            "8501",
            "--server.headless",
            "true"
        ]
    )


# -----------------------------
# Open browser ONCE
# -----------------------------
def open_browser():
    time.sleep(5)
    if not flag.exists():
        webbrowser.open("http://localhost:8501")
        flag.write_text("opened")


# -----------------------------
# Start everything
# -----------------------------
if __name__ == "__main__":
    backend_thread = threading.Thread(target=run_backend, daemon=True)
    backend_thread.start()

    browser_thread = threading.Thread(target=open_browser, daemon=True)
    browser_thread.start()

    run_frontend()
