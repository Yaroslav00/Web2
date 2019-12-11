from rediscluster import RedisCluster

startup_nodes = [{"host": "127.0.0.1", "port": "6379"}]
rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)
rc.set('asd','1')

print(rc.get("foo"))