import sys
import pickle
pickle.HIGHEST_PROTOCOL = 4
from rq import Queue, Worker
from redis import Redis
import task
if __name__ =='__main__':
    print('Worker starts!')
    conn = Redis('127.0.0.1', 6379)
    
    queue = Queue('hull_white_task', connection=conn)
   #s print('Worker starts!')
    worker = Worker([queue], connection=conn)
    worker.work()
       