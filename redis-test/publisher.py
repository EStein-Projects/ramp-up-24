from fastapi import FastAPI
import redis


app = FastAPI()
redis = redis.Redis(decode_responses=True)

if redis.ping():
    print("Connection to Redis successful!")
else:
    print("Connection to Redis failed!")

@app.post("/publish")
async def publish_message(channel: str, message:str):
    redis.publish(channel, message)
    return "message published"