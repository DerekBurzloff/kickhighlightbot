from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
import asyncio
import threading

app = FastAPI(title="KickHighlightBot Dashboard")
templates = Jinja2Templates(directory="templates")

# Global state for bot
bot_running = False
bot_thread = None

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "status": "🟢 Running" if bot_running else "⭕ Stopped"
    })

@app.post("/start")
async def start_bot():
    global bot_running, bot_thread
    if not bot_running:
        bot_running = True
        print("🚀 Bot started!")
        # In real version: start the monitoring thread here
    return {"status": "started"}

@app.post("/stop")
async def stop_bot():
    global bot_running
    bot_running = False
    print("⛔ Bot stopped!")
    return {"status": "stopped"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
