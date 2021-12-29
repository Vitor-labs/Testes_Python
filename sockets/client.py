import time
import socket
import threading

PORT = 5050
HEADER = 64
SERVER = '192.168.224.1'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))


def send(msg):
    message = msg.encode('utf-8')
    length = len(message)
    send_length = str(length).encode('utf-8')
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode('utf-8'))


send("Hello There")
#send("Hello back")
send("!DISCONNECT")
