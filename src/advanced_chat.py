from better_profanity import profanity
from src.config import Config

class AdvancedChat:
    def __init__(self):
        self.config = Config()
        profanity.load_words(["badword1", "badword2"])  # Add your banned words

    def moderate(self, message: str):
        """Return moderation action"""
        if profanity.contains_profanity(message):
            return {"action": "timeout", "reason": "Toxicity detected"}
        
        if any(cmd in message.lower() for cmd in ["!clip", "!highlight"]):
            return {"action": "manual_clip", "reason": "User requested clip"}
        
        return {"action": "allow", "reason": "Clean message"}
