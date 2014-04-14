#!/usr/bin/env python
import sys
import redis
import datetime

redis = redis.StrictRedis(host="localhost", port=6379, db=1)
pipe = redis.pipeline()
for line in sys.stdin:
    pipe.set(line.strip(),str(datetime.date.today()))
    pipe.sadd("MACS",line.strip())
pipe.execute()
