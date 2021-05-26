from multiprocessing import Process, Value, Array, Lock, Pool
import os

def square_numbers():
    for i in range(1000):
        i * i

def basic_example():
    if __name__ == "__main__":
        processes = []
        num_processes = os.cpu_count()
        # Number of CPUs on the machine. Usually a good choise for the number of processes

        # create processes and aisgn a function for each prcoess
        for i in range(num_processes):
            process = Process(target=square_numbers)
            processes.append(process)

        # start all processes
        for process in processes:
            process.start()

        # wait for all processes to finish
        # block the main program until these processes are finished
        for process in processes:
            process.join()
import time

# lock prevents race condition as in threads.
def add_100(number, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        number.value += 1
        lock.release()

def second_example():
    if __name__ == "__main__":
        shared_number = Value('i', 0)
        print('Number at begginning is', shared_number.value)
    lock = Lock()
    p1 = Process(target=add_100, args=(shared_number, lock))
    p2 = Process(target=add_100, args=(shared_number, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('number at end is', shared_number.value)


def add_array_100(numbers, lock):
    for i in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            with lock:
                numbers[i] += 1


def shared_array_example():
    if __name__ == "__main__":
        shared_array = Array('d', [0.0, 100.0, 200.0])
        print('Array at begginning is', shared_array[:])
    lock = Lock()
    p1 = Process(target=add_array_100, args=(shared_array, lock))
    p2 = Process(target=add_array_100, args=(shared_array, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Array at end is', shared_array[:])

from multiprocessing import Queue


def square(numbers, queue):
    for i in numbers:
        queue.put(i*i)


def make_negative(numbers, queue):
    for i in numbers:
        queue.put(-1 * i)


def shared_queue_example():

    numbers = range(1, 6)
    q = Queue()

    p1 = Process(target=square, args=(numbers, q))
    p2 = Process(target=make_negative, args=(numbers, q))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    while not q.empty():
        print(q.get())


def cube(number):
    return number * number * number


def pool_example():
    if __name__ == "__main__":

        numbers = range(10)
        pool = Pool()

        # map, apply, join , close
        result = pool.map(cube, numbers)
        # single_result = pool.apply(cube, numbers[0])
        pool.close()
        pool.join()
        print(result)
        # print(single_result)


# second_example()
# shared_array_example()
# shared_queue_example()
pool_example()