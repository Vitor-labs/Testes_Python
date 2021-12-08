import time
from threading import Thread, Lock

inicial_data = 0


def thread_func(num, lock):
    global inicial_data

    lock.acquire()
    for i in range(10):
        inicial_data += 1
        print('Thread {}: {}'.format(num, inicial_data))
        time.sleep(1)

    lock.release()


def main():
    print('Iniciando o processo principal')
    print('Processo principal: {}'.format(inicial_data))

    lock = Lock()

    thread1 = Thread(target=thread_func, args=(1, lock))
    thread2 = Thread(target=thread_func, args=(2, lock))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Finalizado em ", time.perf_counter(), " segundos")


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
