import redis

def create_redis_client(host, port):
    return redis.Redis(host=host, port=port, decode_responses=True)