from threading import Thread

def square_numbers():
    for i in range(100):
        i * i
        print(i*i, end=", ")
    print("Square numbers done", end="\n")

if __name__ == "__main__":
    threads = []
    num_threads = 10

    # create threads
    for i in range(num_threads):
        thread = Thread(target=square_numbers)
        print(f"create thread {thread.name}", end="\n")
        threads.append(thread)


    # start threads
    for thread in threads:
        print(f"start thread {thread.name}", end="\n")
        thread.start()


    # join threads: wait for them to complete
    for thread in threads:
        print(f"before join thread {thread.name}")
        thread.join()
        print(f"after join thread {thread.name}")

    print('end main')