from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    def __init__(self):
        self.kick_username = "kaesonnguns"
        self.tiktok_username = "kchallin🌺"
        self.xai_api_key = os.getenv("XAI_API_KEY")
        self.discord_webhook = os.getenv("DISCORD_WEBHOOK")
        self.highlight_threshold = os.getenv("HIGHLIGHT_THRESHOLD", "medium")
