import json
import os
from datetime import datetime

def log_qa(user_message, assistant_response):
    os.makedirs('logs', exist_ok=True)
    log_file = f"logs/chat_{datetime.now().strftime('%Y-%m-%d')}.jsonl"
    entry = {
        "timestamp": datetime.now().isoformat(),
        "user": user_message,
        "assistant": assistant_response
    }
    with open(log_file, 'a') as f:
        f.write(json.dumps(entry) + '\n')