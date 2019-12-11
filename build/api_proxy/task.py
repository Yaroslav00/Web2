import time

def example(seconds):
    print('Starting task')
    for i in range(seconds):
        job.meta['progress'] = 100.0 * i / seconds
        job.save_meta()
      
        
    print('Task completed')
    return 20