from fastapi import FastAPI
import uvicorn
import os

app = FastAPI(title="KickHighlightBot")

@app.get("/")
async def root():
    return {
        "status": "🟢 Online",
        "channel": "kaesonnguns",
        "game": "Rainbow Six Siege",
        "message": "Highlight bot ready (stable version)"
    }

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
