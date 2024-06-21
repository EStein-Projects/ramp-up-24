import redis

redis = redis.Redis(decode_responses=True)
pubsub = redis.pubsub()
pubsub.subscribe("ch")
while True:
    message = pubsub.get_message()
    if message:
        print (message)