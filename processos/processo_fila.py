from multiprocessing import Array, Process, Value, Lock, Queue
import os


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def square(numbers, q):
    info('function square')
    for i in numbers:
        q.put(i * i)


def negative(numbers, q):
    info('function negative')
    for i in numbers:
        q.put(-i)


if __name__ == '__main__':
    info('Main line')
    q = Queue()
    numbers = range(6)
    p = Process(target=square, args=(numbers, q))
    p2 = Process(target=negative, args=(numbers, q))

    p.start()
    p2.start()

    p.join()
    p2.join()

    while not q.empty():
        print(q.get())

    info('End of program')

