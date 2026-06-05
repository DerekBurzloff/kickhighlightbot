import re
import time
import random
from collections import defaultdict

class AdvancedChat:
    def __init__(self):
        self.bot_patterns = [
            r"^![\w]+",                    # Bot commands (!play, !song, !rank, etc.)
            r"^\s*\d+\s*$",                # Pure numbers (common bot spam)
            r"^(follow|sub|raid|clip|discord|twitter|youtube|instagram)", 
            r"bot$",                       # Username ends with "bot"
            r"^\s*[!/][\w]+",              # ! or / commands
            r"^(thanks|thank you|ty) (for the|for) (follow|sub|raid)",  # Auto-thank bots
            r"^(welcome|welcoming)",       # Welcome bots
            r"^(now playing|np:)",         # Music bots
            r"^\s*http",                   # Link spam bots
        ]
        
        self.known_bots = {
            "nightbot", "streamlabs", "streamelements", "moobot", "wizebot",
            "songrequest", "musicbot", "giveawaybot", "donationbot", "tipbot"
        }
        
        self.responses = [
            "🤖 Bot detected! How can I help you today?",
            "👋 Hello bot friend!",
            "🔄 Automated response engaged",
            "💬 What's up bot?",
            "🛡️ Bot interaction logged"
        ]
        
        self.last_response = {}

    def is_bot(self, username: str, message: str) -> bool:
        username_lower = username.lower().strip()
        
        if username_lower in self.known_bots:
            return True
        
        message_lower = message.lower()
        for pattern in self.bot_patterns:
            if re.search(pattern, message_lower):
                return True
                
        return False

    def respond_to_bot(self, username: str, message: str):
        now = time.time()
        if username in self.last_response and now - self.last_response[username] < 25:
            return None  # Rate limit
        
        self.last_response[username] = now
        response = random.choice(self.responses)
        
        print(f"🤖 Bot detected → {username}: {message}")
        print(f"💬 Bot Response: {response}")
        
        return response
