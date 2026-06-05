from fastapi import FastAPI
import uvicorn
from src.config import Config
from src.redis_manager import RedisManager

app = FastAPI(title="KickHighlightBot")
config = Config()
redis_manager = RedisManager()

@app.get("/")
async def dashboard():
    recent_clips = redis_manager.get_recent_clips(10)
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head><title>KickHighlightBot</title>
    <style>body{{background:#0a0a0a;color:#eee;font-family:system-ui;}}</style>
    </head>
    <body>
        <h1>🚀 KickHighlightBot</h1>
        <p>Channel: {config.kick_username} • Status: <span style="color:#00ff9d">🟢 Online</span></p>
        <h2>Recent Highlights</h2>
        {"".join([f"<p>📹 {clip.get('filename','clip')}</p>" for clip in recent_clips]) or "<p>No clips yet</p>"}
    </body>
    </html>
    """
    return html

if __name__ == "__main__":
    print("🚀 KickHighlightBot with Redis is running!")
    uvicorn.run(app, host="0.0.0.0", port=8000)
