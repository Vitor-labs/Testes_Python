from multiprocessing import Array, Process, Value, Lock
import os
from rich.console import Console

console = Console()


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
    console.log('\n', log_locals=True)


def add_10(x, valor, lock):
    info('function add_10')
    for i in range(x):
        with lock:
            valor.value += 10
        print('valor', valor.value, '| i: ', i)


def add_array(valor, lock):
    info('function add_array')
    for i in range(len(valor)):
        with lock:
            valor[i] += 1.0
        print('valor', valor[i], '| i: ', i)


if __name__ == '__main__':
    info('main line')
    lock = Lock()
    shared_value = Value('i', 0)
    shared_array = Array('d', [0.3, 0.5, 0.7, 0.8, 1.3])
    print('Valor inicial: ', shared_value.value)
    print('Array inicial: ', shared_array[:])

    p = Process(target=add_10, args=(3, shared_value, lock))
    p2 = Process(target=add_10, args=(2, shared_value, lock))

    p_array = Process(target=add_array, args=(shared_array, lock))
    p2_array = Process(target=add_array, args=(shared_array, lock))

    p.start()
    p2.start()
    p_array.start()
    p2_array.start()

    p.join()
    p2.join()
    p_array.join()
    p2_array.join()

    print('Valor final: ', shared_value.value)
    print('Array final: ', shared_array[:])

    info('end of main line')
