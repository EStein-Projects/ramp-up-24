import redis
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Get the environment variable
redis_host = os.environ.get('REDIS_HOST')

channel: str = "ch"

redis = redis.Redis(host=redis_host, decode_responses=True)
pubsub = redis.pubsub()
pubsub.subscribe(channel)
logger.info("Waiting for messages...")
while True:
    message = pubsub.get_message()
    if message:
        print (message)
        logger.info(f"Received message: {message['data']}")