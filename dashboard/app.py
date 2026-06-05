from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from src.config import Config

app = FastAPI()

config = Config()

@app.get("/", response_class=HTMLResponse)
async def dashboard():
    return f"""
    <h1>KickHighlightBot Dashboard</h1>
    <p>Channel: <strong>{config.kick_username}</strong> (Rainbow Six Siege)</p>
    <p>Status: <span style="color:green">🟢 Running</span></p>
    <p>Auto Captions + Vertical Shorts: Enabled</p>
    <hr>
    <p><em>Full autonomous bot for kaesonnguns → @kchallin🌺</em></p>
    """
