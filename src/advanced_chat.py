
from collections import defaultdict

import time

from src.config import Config

class AdvancedChat:

    def __init__(self):

        self.config = Config()

        self.active_users = defaultdict(lambda: {"last_seen": 0, "reactions": 0})

        self.reaction_emotes = ["🔥", "👑", "💀", "😂", " Pog", "Clap", "Hype"]

    def process_message(self, username: str, message: str):

        now = time.time()

        self.active_users[username]["last_seen"] = now

        

        # Count reactions

        reaction_count = sum(1 for emote in self.reaction_emotes if emote.lower() in message.lower())

        if reaction_count > 0:

            self.active_users[username]["reactions"] += reaction_count

            print(f"🎉 Reaction from {username}: {message}")

        # Return presence summary every 10 messages

        if len(self.active_users) % 10 == 0:

            print(f"👥 Active chatters: {len([u for u in self.active_users if now - self.active_users[u]['last_seen'] < 300])}")

        return {"action": "allow", "presence": len(self.active_users)}

