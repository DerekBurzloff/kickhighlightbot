from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
import os

app = FastAPI(title="KickHighlightBot")
templates = Jinja2Templates(directory="templates")

bot_running = False

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    status = "🟢 Running" if bot_running else "⭕ Stopped"
    return templates.TemplateResponse("index.html", {"request": request, "status": status})

@app.post("/start")
async def start_bot():
    global bot_running
    bot_running = True
    print("🚀 Bot Started!")
    return {"status": "started"}

@app.post("/stop")
async def stop_bot():
    global bot_running
    bot_running = False
    print("⛔ Bot Stopped!")
    return {"status": "stopped"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
