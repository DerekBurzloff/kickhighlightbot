from fastapi import FastAPI
import uvicorn
from src.config import Config

app = FastAPI(title="KickHighlightBot")

config = Config()

@app.get("/")
async def root():
    return {
        "status": "🟢 Online",
        "channel": config.kick_username,
        "message": "Bot is running! Check recent clips in /processed folder"
    }

if __name__ == "__main__":
    print("🚀 KickHighlightBot for kaesonnguns is running!")
    print("Dashboard → http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
