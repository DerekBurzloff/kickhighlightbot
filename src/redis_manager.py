import redis
import json
from datetime import datetime

class RedisManager:
    def __init__(self):
        self.redis = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

    def save_clip(self, clip_data):
        key = f"clip:{int(datetime.now().timestamp())}"
        self.redis.set(key, json.dumps(clip_data))
        self.redis.expire(key, 86400)  # Keep for 24 hours

    def get_recent_clips(self, limit=10):
        keys = self.redis.keys("clip:*")
        clips = []
        for key in sorted(keys, reverse=True)[:limit]:
            data = self.redis.get(key)
            if data:
                clips.append(json.loads(data))
        return clips
