import time
import threading
from multiprocessing import Process, cpu_count


def contar(lim):
    aux = 0
    while aux < lim:
        aux += 1


def main():

    print(cpu_count())

    a = Process(target=contar, args=(1000,))

    print("Iniciando processo contador")
    a.start()
    a.join()

    print("Finalizado em ", time.perf_counter(), " segundos")


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

if __name__ == "__main__":
    main()
