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
        "game": "Rainbow Six Siege"
    }

if __name__ == "__main__":
    print("🚀 Starting KickHighlightBot for kaesonnguns...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
