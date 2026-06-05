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
        recent_clips = sorted([f for f in os.listdir(clips_dir) if f.endswith(".mp4")], reverse=True)[:8]

    clips_html = ""
    for clip in recent_clips:
        clips_html += f'''
        <div style="margin: 20px 0; background: #1a1a1a; padding: 15px; border-radius: 12px;">
            <h3>🎥 {clip}</h3>
            <video width="100%" controls>
                <source src="/processed/{clip}" type="video/mp4">
                Your browser does not support the video tag.
            </video>
        </div>
        '''

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
            .status {{ color: #00ff9d; }}
        </style>
    </head>
    <body>
        <div class="header">
            <div class="logo">KickHighlightBot</div>
            <div><span class="status">● LIVE</span> • {config.kick_username}</div>
        </div>

        <div class="card">
            <h2>📡 Live Status</h2>
            <p><strong>Channel:</strong> {config.kick_username} (Rainbow Six Siege)</p>
            <p><strong>TikTok:</strong> @{config.tiktok_username}</p>
            <p><strong>Status:</strong> <span class="status">🟢 Online & Streaming Highlights</span></p>
        </div>

        <div class="card">
            <h2>🎬 Video Streaming Feed</h2>
            {clips_html or "<p>No clips yet. Go live and get some hype in chat!</p>"}
        </div>
    </body>
    </html>
    """
    return html

if __name__ == "__main__":
    import uvicorn
    print("🚀 KickHighlightBot with Video Streaming is running!")
    uvicorn.run(app, host="0.0.0.0", port=8000)
