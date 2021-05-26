from threading import Thread, Lock, current_thread
import time

database_value = 0

def demo1():
    if __name__ == '__main__':
        threads = []
        num_threads = 10

        # create threads
        for i in range(num_threads):
            thread = Thread(target=square_numbers)
            threads.append(thread)

        # start threads
        for thread in threads:
            thread.start()

        # join threads: wait for them to complete
        for thread in threads:
            thread.join()

        print('end main')


def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)

def increase(lock):
    global database_value
    # lock.acquire()
    with lock:
        local_copy = database_value

        # processing
        local_copy += 1
        time.sleep(0.1)

        database_value = local_copy
    # lock.release()

def demo2():

    global database_value
    if __name__ == '__main__':

        lock = Lock()
        print('start value', database_value)

        thread1 = Thread(target=increase, args=(lock,))
        thread2 = Thread(target=increase, args=(lock,))

        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()

        print('end value', database_value)

        print('end main')

# demo2()

from queue import Queue

# using queue for tread safe

def worker(q, lock):
    while True:
        value = q.get()

        # processing..
        with lock:
            print(f'in {current_thread().name} got {value}')
            q.task_done()

def demo3():
    print("START DEMO 3")

    q = Queue()
    lock = Lock()
    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q,lock))
        thread.daemon = True
        thread.start()

    for i in range(1, 21):
        q.put(i)

    q.join()
    print("END DEMO 3")

def qeueuExample():
    q = Queue()

    q.put(1)
    q.put(2)
    q.put(3)

    # 3 2 1 --->
    first = q.get()
    print(first)

    q.task_done()
    q.join()

demo3()