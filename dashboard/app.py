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
    clips_dir = "processed"
    recent_clips = []
    if os.path.exists(clips_dir):
        recent_clips = sorted([f for f in os.listdir(clips_dir) if f.endswith(".mp4")], reverse=True)[:8]

    return templates.TemplateResponse("index.html", {
        "request": request,
        "channel": config.kick_username,
        "tiktok": config.tiktok_username,
        "status": "🟢 Online",
        "recent_clips": recent_clips
    })
