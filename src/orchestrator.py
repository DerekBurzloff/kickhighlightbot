import os
import time
from src.kick_monitor import KickMonitor
from src.highlight_detector import HighlightDetector
from src.clip_processor import ClipProcessor
from src.tiktok_uploader import TikTokUploader

class Orchestrator:
    def __init__(self):
        self.monitor = KickMonitor()
        self.detector = HighlightDetector()
        self.processor = ClipProcessor()
        self.uploader = TikTokUploader()

    def run_cycle(self):
        try:
            print("🔄 Running full highlight detection cycle...")
            chat_messages = self.monitor.check_chat()

            for msg in chat_messages:
                print(f"💬 Chat: {msg}")
                if self.detector.detect(msg):
                    print(f"🔥 HYPE DETECTED: {msg}")
                    # Create clip (using test clip for now)
                    short = self.processor.create_vertical_short('test_clip.mp4')
                    if short:
                        self.uploader.upload(short)
        except Exception as e:
            print(f"❌ Error in cycle: {e}")
