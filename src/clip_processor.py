import subprocess
import os
from src.caption_generator import CaptionGenerator

class ClipProcessor:
    def __init__(self):
        self.caption_gen = CaptionGenerator()

    def create_vertical_short(self, input_path: str, output_path: str = None):
        if not os.path.exists(input_path):
            print("❌ Input video not found")
            return None

        if output_path is None:
            output_path = f"processed/final_short_{int(os.path.getmtime(input_path))}.mp4"

        captions = self.caption_gen.generate_hype_captions("Rainbow Six Siege play")
        caption_text = " • ".join([c.replace("'", "") for c in captions[:2]])

        print(f"🎤 Grok Captions: {caption_text}")

        # Simple vertical conversion (reliable)
        cmd = [
            'ffmpeg', '-i', input_path,
            '-vf', "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2",
            '-c:v', 'libx264', '-preset', 'fast', '-crf', '23',
            '-c:a', 'aac', '-y', output_path
        ]

        try:
            subprocess.run(cmd, check=True, capture_output=True, text=True)
            print(f"✅ Vertical Short created: {output_path}")
            print(f"   Captions ready: {caption_text}")
            return output_path
        except Exception as e:
            print(f"❌ Error: {e}")
            return None
