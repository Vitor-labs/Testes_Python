import time
import random
import logging
from queue import Queue
from concurrent.futures import ThreadPoolExecutor
from threading import Thread, Lock, current_thread


def worker_thread(q):
    tname = current_thread().name
    logging.info('Starting Worker [{tname}] Thread')
    try:
        item = random.randint(1, 10)
        logging.info('{} got {}'.format(tname, item))
        with Lock():
            q.put(item)
    except:
        logging.info('Worker Thread %s failed', tname)
        raise
    finally:
        q.task_done()
        logging.info('Worker Thread %s finished', tname)


def queue_thread():
    logging.info('Starting Queue Thread')
    q = Queue()
    t = Thread(target=worker_thread, args=(q,))
    t.start()
    logging.info('Starting Thread')
    t.join()
    ret = q.get()
    logging.info('Got %s from %s', ret, t.name)


def main():
    logging.basicConfig(
        level=logging.DEBUG, format='%(levelthread)s: %(asctime)s [%(threadthread)s] -> %(message)s', datefmt='%H:%M:%S')
    logging.info('Starting Main Thread')
    queue_thread()


if __name__ == "__main__":
    main()
