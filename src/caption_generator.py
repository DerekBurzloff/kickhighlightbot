from openai import OpenAI
import os

class CaptionGenerator:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("XAI_API_KEY"),
            base_url="https://api.x.ai/v1"
        )

    def generate_hype_captions(self, transcript: str = "Great Rainbow Six Siege moment"):
        """Generate exciting R6 Siege TikTok captions using Grok"""
        prompt = f"""
        You are a professional TikTok editor for Rainbow Six Siege clips.
        Create 3-5 short, high-energy overlay captions perfect for vertical Shorts.
        Make them hype, use emojis, caps, and gaming slang.

        Clip context: {transcript}

        Output format: One caption per line.
        """

        try:
            response = self.client.chat.completions.create(
                model="grok-4",          # You can also try "grok-3" or latest
                messages=[{"role": "user", "content": prompt}],
                max_tokens=400,
                temperature=0.85
            )
            captions = response.choices[0].message.content.strip().split("\n")
            return [c.strip() for c in captions if c.strip()]
        except Exception as e:
            print(f"⚠️ Grok API error: {e}")
            return ["INSANE CLUTCH 🔥", "ACE BABY!", "WHAT A FLICK!"]
