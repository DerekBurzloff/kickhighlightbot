from fastapi import FastAPI
import uvicorn
from src.config import Config
from src.highlight_detector import HighlightDetector

app = FastAPI(title="KickHighlightBot - R6 Siege")

config = Config()
detector = HighlightDetector()

@app.get("/")
async def root():
    return {
        "status": "🟢 Online",
        "channel": config.kick_username,
        "game": "Rainbow Six Siege",
        "status_message": "Waiting for highlights..."
    }

if __name__ == "__main__":
    print("🚀 KickHighlightBot started for kaesonnguns")
    print("Dashboard: http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
