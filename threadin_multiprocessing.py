"""
    Process: An instance of a program

    + Takes advantage of multiple CPUs and cores
    + great for CPU-bound processing
    + new Process is started independently from other process
    + Processes are interruptable/killable
    + One GIL for each process -> avoid GIL limitation

    Disadvantages
    - Heavyweight
    - Starting a process is slower than starting a thread
    - More memory
    - IPC (inner-process communication) is more complicated

"""

"""
    Threads: An entity within a process that can be scheduled (also known as "lightweight" process)
    A process can spawn multiple threads 
    
    + All thread within a process share the same memory
    + Lightweight
    + Starting a thread is faster than starting a process
    + Great for I\O-bound tasks
    
    - Threading is limited by GIL: Only one thread at a time
    - No effect for CPU-bound tasks
    - Not Interruptable/killable
    - Careful with race conditions
"""

"""
    GIL: Global interpreter lock
    - A lock that allows only one thread at a time to execute in Python
    - Needed in CPython because memory management is not thread-safe
    
    Avoid:
    - Use multiprocessing
    - Use a different, free-threaded Python implementation (Jython, IronPython)
    - use Python as a wrapper for third-party libraries (C/C++) -> numpy, scipy
"""

from multiprocessing import Process
import os
import time

def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)



processes = []
num_processes = os.cpu_count()

#create processes
for i in range(num_processes):
    p = Process(target=square_numbers)
    processes.append(p)

# start
for p in processes:
    p.start()

# join
for p in processes:
    p.join()

print('end main processes')


from threading import Thread
def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)



threads = []
num_threads = 10

#create threads
for i in range(num_threads):
    t = Thread(target=square_numbers)
    threads.append(t)

# start
for t in threads:
    t.start()

# join
for t in threads:
    t.join()

print('end main threads')
