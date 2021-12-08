import time
from queue import Queue
from threading import Thread, Lock, current_thread


def worker_thread(q, lock):
    while True:
        item = q.get()
        with lock:
            print(f'{current_thread().name} - {item}')
        q.task_done()


if __name__ == "__main__":
    q = Queue()
    lock = Lock()

    t = 5
    for i in range(t):
        thread1 = Thread(target=worker_thread, args=(q, lock))
        thread1.daemon = True
        thread1.start()

    for i in range(100):
        q.put(i)

    q.join()

    print("Fim")
