import socket
import time
import threading
from queue import Queue

socket.setdefaulttimeout(0.55)

print_lock = threading.Lock()

target = input('Host to scan: ')

t_IP = socket.gethostbyname(target)
print('Scanning Host for Open Ports: ', t_IP)

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        conx = s.connect((t_IP, port))
        with print_lock:
            print(port, 'is open')
        conx.close()
    except:
        pass

def threader():
    worker = q.get()
    portscan(worker)
    q.task_done()

q = Queue()
start_time = time.time()
for x in range(200):
    t = threading.Thread(target = threader)
    t.daemon = True
    t.start()

for worker in range(1, 65535):
    q.put(worker)
q.join()

runtime = float("%0.2f" %(time.time() - startTime))
print("Run Time: ", runtime, "seconds")
