from fastapi import FastAPI
import uvicorn
import os
from src.config import Config

app = FastAPI(title="KickHighlightBot")

config = Config()

@app.get("/")
async def dashboard():
    clips_dir = "processed"
    recent_clips = []
    if os.path.exists(clips_dir):
        recent_clips = sorted([f for f in os.listdir(clips_dir) if f.endswith(".mp4")], reverse=True)[:8]

    html = f"""
    <h1>🚀 KickHighlightBot</h1>
    <p><strong>Status:</strong> 🟢 Online</p>
    <p><strong>Channel:</strong> {config.kick_username}</p>
    <p><strong>TikTok:</strong> @{config.tiktok_username}</p>
    <h2>Recent Clips</h2>
    """
    if recent_clips:
        for clip in recent_clips:
            html += f"<p>📹 <a href='/processed/{clip}' target='_blank'>{clip}</a></p>"
    else:
        html += "<p>No clips yet. Start streaming!</p>"

    return HTMLResponse(html)

from fastapi.responses import HTMLResponse

if __name__ == "__main__":
    print("🚀 KickHighlightBot is running!")
    uvicorn.run(app, host="0.0.0.0", port=8000)
