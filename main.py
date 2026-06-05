from fastapi import FastAPI
import uvicorn
from src.config import Config
from src.highlight_detector import HighlightDetector
from src.clip_processor import ClipProcessor
from src.kick_monitor import KickMonitor

app = FastAPI(title="KickHighlightBot - R6 Siege")

config = Config()
detector = HighlightDetector()
processor = ClipProcessor()
monitor = KickMonitor()

@app.get("/")
async def root():
    return {
        "status": "🟢 Online",
        "channel": config.kick_username,
        "game": "Rainbow Six Siege",
        "message": "Bot is monitoring for highlights!"
    }

if __name__ == "__main__":
    print("🚀 KickHighlightBot for kaesonnguns is now running!")
    print("→ Dashboard: http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
