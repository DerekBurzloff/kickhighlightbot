from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    def __init__(self):
        self.kick_username = "kaesonnguns"
        self.tiktok_username = "kchallin🌺"
        self.openai_key = os.getenv("OPENAI_API_KEY")
        self.highlight_threshold = os.getenv("HIGHLIGHT_THRESHOLD", "medium")
