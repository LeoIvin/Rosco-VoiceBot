import datetime

LOG_FILE = "Ricoso_Logs/conversation_log.txt"

def log_conversation(speaker, text):
    """
    Logs a line of conversation to the log file.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {speaker}: {text}\n") 