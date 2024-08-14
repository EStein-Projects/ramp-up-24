from fastapi import FastAPI
import redis
import os

# Get the environment variable
redis_host = os.environ.get('REDIS_HOST')

app = FastAPI()
redis = redis.Redis(host=redis_host, decode_responses=True)

@app.post("/publish")
async def publish_message(channel: str, message: str):
    redis.publish(channel, message)
    return "message published"