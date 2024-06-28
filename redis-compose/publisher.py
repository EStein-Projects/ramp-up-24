from fastapi import FastAPI
import redis


app = FastAPI()
redis = redis.Redis(decode_responses=True)


@app.post("/publish")
async def publish_message(channel: str, message: str):
    redis.publish(channel, message)
    return "message published"