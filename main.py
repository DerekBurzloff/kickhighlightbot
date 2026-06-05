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
        recent_clips = sorted([f for f in os.listdir(clips_dir) if f.endswith(".mp4")], reverse=True)[:10]

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>KickHighlightBot • Live</title>
        <style>
            body {{ font-family: 'Inter', system-ui; background: #0a0a0a; color: #e0e0e0; margin: 0; padding: 20px; }}
            .header {{ display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #333; padding-bottom: 20px; }}
            .status {{ color: #00ff9d; font-weight: bold; }}
            .card {{ background: #1a1a1a; border-radius: 12px; padding: 20px; margin: 15px 0; }}
            h1 {{ color: #00ff9d; }}
            .clip {{ padding: 12px; background: #222; border-radius: 8px; margin: 8px 0; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>🚀 KickHighlightBot</h1>
            <div><span class="status">● LIVE</span></div>
        </div>

        <div class="card">
            <p><strong>Channel:</strong> {config.kick_username} (Rainbow Six Siege)</p>
            <p><strong>TikTok:</strong> @{config.tiktok_username}</p>
            <p><strong>Status:</strong> <span class="status">Online & Monitoring Chat</span></p>
        </div>

        <h2>📼 Recent Highlights</h2>
        {"".join([f'<div class="clip">📹 <a href="/processed/{clip}" target="_blank">{clip}</a></div>' for clip in recent_clips]) or "<p>No clips yet. Start streaming and get some hype in chat!</p>"}
        
        <p style="margin-top: 30px; color: #666; font-size: 0.9em;">
            Bot is running 24/7 • Clips saved in /processed folder
        </p>
    </body>
    </html>
    """
    return html

if __name__ == "__main__":
    import uvicorn
    print("🚀 KickHighlightBot is running!")
    print("Dashboard: http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
