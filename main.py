from fastapi import FastAPI
import uvicorn
from src.config import Config
from dashboard.app import dashboard_app  # Import the dashboard

app = FastAPI(title="KickHighlightBot")

config = Config()

# Mount the dashboard
app.mount("/", dashboard_app)

if __name__ == "__main__":
    print("🚀 KickHighlightBot for kaesonnguns is running!")
    print("Dashboard → http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
