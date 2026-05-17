import datetime

def log_history(entry):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("history.txt", "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {entry}\n")
