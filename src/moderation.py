from better_profanity import profanity
import re

class ModerationEngine:
    def __init__(self):
        profanity.load_words(["spam", "bot", "raid"])
    
    def moderate(self, username, message):
        if profanity.contains_profanity(message):
            return {"action": "timeout", "duration": 300, "reason": "Toxicity"}
        
        if re.search(r'(!raid|!follow|sub raid)', message.lower()):
            return {"action": "warn", "reason": "Possible raid bot"}
        
        return {"action": "allow"}
