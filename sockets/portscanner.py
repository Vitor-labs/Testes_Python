import queue
from threading import Thread
from queue import Queue
import socket

# REMENBER TO CHANGE THE IP ADDRESS
# THIS IS ONLY FOR TESTING PURPOSES
# ON PRIVATE NETWORKS, DO NOT USE
# ON PUBLIC NETWORKS.

target = '127.0.0.1'
queue = Queue()
ports_open = []


def port_scanner(port) -> bool:
    try:
        socket_scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_scan.connect((target, port))
        return True
    except:
        return False


def fill_queue(ports):
    for port in ports:
        queue.put(port)


def worker():
    while not queue.empty():
        port = queue.get()
        if port_scanner(port):
            print('Port {} is open'.format(port))
            ports_open.append(port)


def main():
    print('Scanning ports on {}'.format(target))
    ports = range(1, 8080)
    fill_queue(ports)
    threads = []
    for i in range(100):
        thread = Thread(target=worker)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    print(f'\n OPEN PORTS: {ports_open}')


if __name__ == '__main__':
    main()
