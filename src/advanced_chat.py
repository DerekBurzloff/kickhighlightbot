import re
import time
from collections import defaultdict

class AdvancedChat:
    def __init__(self):
        self.bot_patterns = [
            r"^![\w]+",           # Common bot commands (!play, !rank, etc.)
            r"^\s*\d+\s*$",       # Just numbers (some bots spam)
            r"^(follow|sub|raid|clip|discord)",  # Common bot phrases
            r"bot$",              # Username ends with "bot"
        ]
        self.known_bots = {"nightbot", "streamlabs", "streamelements", "moobot", "wizebot"}
        self.responses = [
            "👋 Hey there bot!",
            "🤖 Bot detected! What's up?",
            "🔄 Automated response activated",
            "💬 Human or bot? 😏"
        ]
        self.last_response = {}

    def is_bot(self, username: str, message: str) -> bool:
        username_lower = username.lower()
        if username_lower in self.known_bots:
            return True
        
        for pattern in self.bot_patterns:
            if re.search(pattern, message.lower()):
                return True
        return False

    def respond_to_bot(self, username: str, message: str):
        now = time.time()
        if username in self.last_response and now - self.last_response[username] < 30:
            return None  # Rate limit responses
        
        self.last_response[username] = now
        import random
        response = random.choice(self.responses)
        print(f"🤖 Bot detected ({username}): {message}")
        print(f"💬 Responding: {response}")
        return response
