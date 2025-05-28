import redis
import json
from datetime import datetime

class SharedMemory:
    def __init__(self, host='localhost', port=6379):
        self.redis = redis.Redis(host=host, port=port, db=0)

    def log(self, key, data):
        timestamp = datetime.utcnow().isoformat()
        data['timestamp'] = timestamp
        self.redis.set(key, json.dumps(data))

    def retrieve(self, key):
        val = self.redis.get(key)
        return json.loads(val) if val else None 
