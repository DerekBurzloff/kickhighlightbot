#!/bin/bash
cd ~/kickhighlightbot

echo "🚀 Starting KickHighlightBot in background..."

# Use full python path and install if needed
nohup python3 -m uvicorn main:app --host 0.0.0.0 --port 8000 > bot.log 2>&1 &

echo "✅ Bot started in background!"
echo "📋 Check logs: tail -f bot.log"
echo "⛔ Stop: pkill -f uvicorn"
