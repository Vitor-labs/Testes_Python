import time
import random
import logging
import threading
from concurrent.futures import ThreadPoolExecutor

count = 0


def test(test_item, num):
    s = random.randrange(1, num)
    logging.info(
        f'Thread {test_item}: id = {threading.get_ident()}')
    logging.info(f'Thread {test_item}: sleeping for {s} secs')
    time.sleep(s)
    global count
    logging.info(f'Thread {test_item}: finished')
    # this is the critical section
    with threading.Lock():
        logging.info(
            f'[{threading.current_thread().name}] {test_item}: got the lock')
        count += 1

    # it is the only place where the count is incremented


def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(levelname)s: %(asctime)s [%(threadName)s] -> %(message)s',
        datefmt='%H:%M:%S')

    logging.info('Stating Main')

    workers = 4
    # itens = 24

    logging.info(f'Starting {workers} workers')
    with ThreadPoolExecutor(max_workers=workers) as executor:
        for i in range(10):
            executor.submit(test, i, 2)

    # with ThreadPoolExecutor(max_workers=workers) as exc:
    #     exc.map(test, range(itens), [
    #             random.randrange(1, 10) for _ in range(itens)])

    # WHIT THE EXECUTOR, THIS PART IS NO LONGER NEEDED
    # threads = []
    # for _ in range(5):
    #     thread = Thread(target=test, args=(_, 3))
    #     threads.append(thread)
    #     thread.start()

    # for _ in threads:
    #     _.join()

    logging.info('Finished in {} secs, counted {}'.format(
        time.perf_counter(), count))
    logging.info('Ending Main')


if __name__ == '__main__':
    main()
