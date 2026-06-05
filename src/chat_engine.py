from better_profanity import profanity
import re
import time

class ChatEngine:
    def __init__(self):
        profanity.load_words(["spam", "raid", "followbot"])
        self.recent_messages = []

    def moderate(self, username, message):
        lower = message.lower()
        if profanity.contains_profanity(lower):
            return {"action": "timeout", "duration": 600, "reason": "Toxicity detected"}

        if re.search(r'(!raid|sub raid|raid here)', lower):
            return {"action": "warn", "reason": "Possible raid"}

        if len(lower) > 200:
            return {"action": "delete", "reason": "Spam"}

        return {"action": "allow"}
