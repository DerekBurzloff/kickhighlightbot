import redis
import json
import os
from datetime import datetime

class RedisManager:
    def __init__(self):
        self.redis = redis.Redis(
            host=os.getenv("REDIS_HOST", "localhost"),
            port=int(os.getenv("REDIS_PORT", 6379)),
            db=0,
            decode_responses=True
        )

    def save_clip(self, clip_data):
        """Save clip info"""
        key = f"clip:{int(datetime.now().timestamp())}"
        self.redis.set(key, json.dumps(clip_data))
        self.redis.expire(key, 86400)  # 24 hours

    def get_recent_clips(self, limit=10):
        """Get recent clips"""
        keys = self.redis.keys("clip:*")
        clips = []
        for key in sorted(keys, reverse=True)[:limit]:
            data = self.redis.get(key)
            if data:
                clips.append(json.loads(data))
        return clips

    def track_user_activity(self, username):
        """Track active users"""
        key = f"user:{username}"
        self.redis.hset(key, "last_seen", str(datetime.now()))
        self.redis.expire(key, 1800)  # 30 minutes
