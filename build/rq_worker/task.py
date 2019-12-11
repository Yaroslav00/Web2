import time
from rq import get_current_job
def example(seconds):
    job = get_current_job()
    print('Starting task')
    answ = 0
    for i in range(seconds):
        job.meta['progress'] = 100.0 * i / seconds
        job.save_meta()
        print(i)
        time.sleep(1)
        answ += i
    
    print('Task completed')
    return answ