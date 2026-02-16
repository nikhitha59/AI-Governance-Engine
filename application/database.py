import sqlite3
from datetime import datetime

# connect database
conn = sqlite3.connect("chat_logs.db", check_same_thread=False)
cursor = conn.cursor()

# create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_message TEXT,
    ai_response TEXT,
    timestamp TEXT
)
""")

conn.commit()

# logging function
def log_interaction(user_message, ai_response):
    cursor.execute(
        "INSERT INTO logs (user_message, ai_response, timestamp) VALUES (?, ?, ?)",
        (user_message, ai_response, datetime.utcnow().isoformat())
    )
    conn.commit()
