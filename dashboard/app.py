from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from src.config import Config
import os

app = FastAPI(title="KickHighlightBot Dashboard")
templates = Jinja2Templates(directory="dashboard/templates")
config = Config()

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    # Get recent clips
    clips_dir = "processed"
    recent_clips = []
    if os.path.exists(clips_dir):
        recent_clips = [f for f in os.listdir(clips_dir) if f.endswith(".mp4")][-5:]  # last 5 clips

    return templates.TemplateResponse("index.html", {
        "request": request,
        "channel": config.kick_username,
        "tiktok": config.tiktok_username,
        "status": "🟢 Online",
        "recent_clips": recent_clips
    })
