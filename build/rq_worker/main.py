import subprocess
import os

if __name__ == "__main__":
    for i in range(2):
        #os.spawnl(os.P_NOWAITO, 'python3 worker.py', os.environ)
        proc = subprocess.call(['xterm -e python3 worker.py'], cwd='./', shell=True)
        