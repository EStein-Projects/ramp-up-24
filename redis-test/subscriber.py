import redis


channel: str = "ch"

redis = redis.Redis(decode_responses=True)
pubsub = redis.pubsub()
pubsub.subscribe(channel)
while True:
    message = pubsub.get_message()
    if message:
        print (message)