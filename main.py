from fastapi import FastAPI
import uvicorn
import threading
import time
from src.config import Config
from src.orchestrator import Orchestrator

app = FastAPI(title="KickHighlightBot")

config = Config()
orchestrator = Orchestrator()

@app.get("/")
async def root():
    return {"status": "🟢 Online", "channel": config.kick_username}

def background_loop():
    print("🚀 Starting full autonomous loop...")
    while True:
        orchestrator.run_cycle()
        time.sleep(15)  # Check every 15 seconds

if __name__ == "__main__":
    # Start background thread
    thread = threading.Thread(target=background_loop, daemon=True)
    thread.start()
    
    print("🚀 KickHighlightBot for kaesonnguns is running!")
    print("Dashboard → http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
