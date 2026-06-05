import time
import random

class KickMonitor:
    def __init__(self):
        self.channel = "kaesonnguns"

    def check_chat(self):
        """Simulate / real chat monitoring"""
        print(f"📡 Checking chat for {self.channel}...")
        
        # For now: simulate some chat messages (later replace with real WebSocket)
        fake_chat = [
            "boring game",
            "INSANE CLUTCH!!!",
            "ACE BABY 🔥",
            "nice flick",
            "1v5 clutch no way"
        ]
        
        # Randomly return a message
        message = random.choice(fake_chat)
        print(f"💬 Chat: {message}")
        return [message]
