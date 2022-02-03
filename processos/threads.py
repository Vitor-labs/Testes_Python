import time
import logging
import random
from threading import Thread, Lock
import os
from rich.console import Console

console = Console()


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
    console.log('\n', log_locals=True)


inicial_data = 0
counter = 0


def long_task(num, name):
    info('long_task')
    max = random.randrange(1, num)
    start = time.time()
    logging.info('Task {} started'.format(name))
    logging.info('Task {}: have {} mini-tasks'.format(name, max))

    for i in range(max):
        thread_func(i, Lock())
        global counter
        counter += 1
        logging.info('Mini-Task {} finished'.format(i))

    logging.info('Task {} completed in {}\n'.format(name, time.time() - start))


def thread_func(num, lock):
    info('thread_func')
    global inicial_data
    with lock:
        inicial_data += 2
        print('Thread {}: {}'.format(num, inicial_data))


def main():
    info('main')
    logging.basicConfig(
        level=logging.DEBUG, format='%(levelname)s: %(asctime)s [%(threadName)s] -> %(message)s', datefmt='%H:%M:%S')

    logging.info('Stating Main')
    logging.info('Initial data: {}'.format(inicial_data))
    long_task(10, 'Task unique')

    threads = []
    for _ in range(5):
        thread = Thread(target=long_task, args=(
            3, 'do something {}'.format(_)))
        threads.append(thread)
        thread.start()

    for _ in threads:
        _.join()

    logging.info('Final data: {}, Counted {}'.format(inicial_data, counter))
    logging.info('Ending Main, Finished in {}'.format(time.perf_counter()))


if __name__ == "__main__":
    main()


# def timer():
#     print()
#     counter = 0
#     while True:
#         time.sleep(1)
#         counter += 1
#         print(counter, "s:")


# def eat():
#     time.sleep(3)
#     print("   uff..... it was good")


# def coffee():
#     time.sleep(4)
#     print("   now im ready !!!")


# def study():
#     time.sleep(5)
#     print("   man..... that's boring...")


# x = threading.Thread(target=timer, daemon=True)
# x.start()

# x1 = threading.Thread(target=eat, args=())
# x2 = threading.Thread(target=coffee, args=())
# x3 = threading.Thread(target=study, args=())

# x1.start()
# x2.start()
# x3.start()

# # x1.join()
# # x2.join()
# # x3.join()

# print(threading.active_count())
# print(threading.enumerate())
# print(time.perf_counter())
