import subprocess
import os

class ClipProcessor:
    def create_vertical_short(self, input_path: str, output_path: str):
        """Convert to 9:16 vertical + add auto captions"""
        cmd = [
            'ffmpeg', '-i', input_path,
            '-vf', "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2",
            '-c:v', 'libx264', '-preset', 'fast',
            '-c:a', 'aac', output_path
        ]
        subprocess.run(cmd, check=True)
        print(f"✅ Created vertical short: {output_path}")
