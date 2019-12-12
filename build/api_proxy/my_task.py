import time
from rq import get_current_job
def hull_white(sigma, shift, period):
    job = get_current_job()
    print('Starting task')
    period = int(period)
    answ = 0
    print(period)
    for i in range(period):
        job.meta['progress'] = 100.0 * i / period
        job.save_meta()
        answ += i
    
    print('Task completed')
    return answ