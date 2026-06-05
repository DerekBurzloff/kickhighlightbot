import time
from src.kick_monitor import KickMonitor
from src.highlight_detector import HighlightDetector
from src.clip_processor import ClipProcessor
from src.tiktok_uploader import TikTokUploader
from src.advanced_chat import AdvancedChat

class Orchestrator:
    def __init__(self):
        self.monitor = KickMonitor()
        self.detector = HighlightDetector()
        self.processor = ClipProcessor()
        self.uploader = TikTokUploader()
        self.chat = AdvancedChat()

    def run_cycle(self):
        try:
            messages = self.monitor.check_chat()
            for msg in messages:
                # Process with advanced chat
                result = self.chat.process_message("chat_user", msg)
                print(f"💬 {msg}")

                if self.detector.detect(msg):
                    print(f"🔥 HYPE DETECTED!")
                    short = self.processor.create_vertical_short('test_clip.mp4')
                    if short:
                        self.uploader.upload(short)
        except Exception as e:
            print(f"Error: {e}")
