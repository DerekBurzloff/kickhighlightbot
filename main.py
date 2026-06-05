from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from src.config import Config
import os
import time

app = FastAPI(title="KickHighlightBot")
config = Config()

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    clips_dir = "processed"
    recent_clips = []
    if os.path.exists(clips_dir):
        recent_clips = sorted([f for f in os.listdir(clips_dir) if f.endswith(".mp4")], reverse=True)[:10]

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>KickHighlightBot • Live</title>
        <meta charset="UTF-8">
        <style>
            body {{ font-family: system-ui; background: #0a0a0a; color: #e0e0e0; margin: 0; padding: 0; }}
            .header {{ background: linear-gradient(90deg, #1a1a1a, #2a2a2a); padding: 20px; display: flex; justify-content: space-between; align-items: center; }}
            .logo {{ font-size: 28px; font-weight: bold; color: #00ff9d; }}
            .status {{ color: #00ff9d; font-weight: bold; }}
            .container {{ padding: 30px; max-width: 1200px; margin: 0 auto; }}
            .card {{ background: #1a1a1a; border-radius: 16px; padding: 24px; margin-bottom: 24px; border: 1px solid #333; }}
            .activity {{ background: #222; padding: 16px; border-radius: 12px; margin: 12px 0; display: flex; align-items: center; }}
            .clip-link {{ color: #00ccff; text-decoration: none; }}
        </style>
    </head>
    <body>
        <div class="header">
            <div class="logo">KickHighlightBot</div>
            <div><span class="status">● LIVE</span> • {config.kick_username}</div>
        </div>

        <div class="container">
            <div class="card">
                <h2>📡 Live Activity Feed</h2>
                <p><strong>Channel:</strong> {config.kick_username} (Rainbow Six Siege)</p>
                <p><strong>TikTok:</strong> @{config.tiktok_username}</p>
            </div>

            <div class="card">
                <h2>📼 Recent Highlights</h2>
                {"".join([f'<div class="activity">🔥 <a class="clip-link" href="/processed/{clip}" target="_blank">{clip}</a></div>' for clip in recent_clips]) or "<p>No clips yet. Go live and get some hype!</p>"}
            </div>
        </div>
    </body>
    </html>
    """
    return html

if __name__ == "__main__":
    import uvicorn
    print("🚀 KickHighlightBot is running!")
    uvicorn.run(app, host="0.0.0.0", port=8000)
