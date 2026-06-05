from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from src.config import Config
import os
import time

app = FastAPI(title="KickHighlightBot")
config = Config()

# Simulate recent chat (in real version this would pull from Redis or WebSocket)
recent_chat = [
    {"user": "kaesonnguns_fan", "message": "INSANE CLUTCH!!! 🔥", "time": "just now"},
    {"user": "r6addict", "message": "1v5 no way bro", "time": "1m ago"},
    {"user": "acehunter", "message": "ACE BABY 👑", "time": "2m ago"},
]

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    clips_dir = "processed"
    recent_clips = []
    if os.path.exists(clips_dir):
        recent_clips = sorted([f for f in os.listdir(clips_dir) if f.endswith(".mp4")], reverse=True)[:8]

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>KickHighlightBot • Live</title>
        <meta charset="UTF-8">
        <style>
            body {{ font-family: system-ui; background: #0a0a0a; color: #eee; margin: 0; padding: 20px; }}
            .header {{ background: #1a1a1a; padding: 20px; border-bottom: 1px solid #333; display: flex; justify-content: space-between; }}
            .logo {{ font-size: 28px; font-weight: bold; color: #00ff9d; }}
            .card {{ background: #1a1a1a; padding: 24px; border-radius: 16px; margin: 20px 0; }}
            .chat-msg {{ background: #222; padding: 12px; border-radius: 8px; margin: 8px 0; }}
            .clip {{ background: #222; padding: 16px; border-radius: 12px; margin: 12px 0; }}
        </style>
    </head>
    <body>
        <div class="header">
            <div class="logo">KickHighlightBot</div>
            <div><span style="color:#00ff9d">● LIVE</span> • {config.kick_username}</div>
        </div>

        <div class="card">
            <h2>💬 Live Chat Feed</h2>
            {"".join([f'<div class="chat-msg"><strong>{msg["user"]}</strong>: {msg["message"]} <small>{msg["time"]}</small></div>' for msg in recent_chat])}
        </div>

        <div class="card">
            <h2>📼 Recent Video Highlights</h2>
            {"".join([f'<div class="clip">🎥 <a href="/processed/{clip}" target="_blank">{clip}</a></div>' for clip in recent_clips]) or "<p>No clips yet. Go live!</p>"}
        </div>
    </body>
    </html>
    """
    return html

if __name__ == "__main__":
    import uvicorn
    print("🚀 KickHighlightBot with Live Chat Feed is running!")
    uvicorn.run(app, host="0.0.0.0", port=8000)
