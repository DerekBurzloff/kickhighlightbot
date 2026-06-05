from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from src.config import Config
import os

app = FastAPI(title="KickHighlightBot")
config = Config()

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    clips_dir = "processed"
    recent_clips = []
    if os.path.exists(clips_dir):
        recent_clips = sorted([f for f in os.listdir(clips_dir) if f.endswith(".mp4")], reverse=True)[:12]

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
            .clip {{ background: #222; padding: 16px; border-radius: 12px; margin: 12px 0; }}
            .status {{ color: #00ff9d; }}
        </style>
    </head>
    <body>
        <div class="header">
            <div class="logo">KickHighlightBot</div>
            <div><span class="status">● LIVE</span> • {config.kick_username}</div>
        </div>

        <div class="card">
            <h2>📡 Live Activity Feed</h2>
            <p>Monitoring chat • Detecting hype • Creating clips automatically</p>
        </div>

        <div class="card">
            <h2>📼 Recent Video Highlights</h2>
            {"".join([f'<div class="clip">🎥 <a href="/processed/{clip}" target="_blank">{clip}</a></div>' for clip in recent_clips]) or "<p>No clips yet. Go live and get some hype!</p>"}
        </div>
    </body>
    </html>
    """
    return html

if __name__ == "__main__":
    import uvicorn
    print("🚀 KickHighlightBot is running with advanced chat & feeds!")
    uvicorn.run(app, host="0.0.0.0", port=8000)
