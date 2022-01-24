import time
import socket
import json


class User:
    name = "user"
    password = ""
    age = 0

    def __init__(self, name, password, age):
        self.name = name
        self.password = password
        self.age = age

    def __str__(self):
        return f"[{time.time()}]: {self.name} {self.password} {self.age}"


PORT = 5050
HEADER = 64
SERVER = 'localhost'

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


def send_obj(obj):
    message = json.dumps(obj)
    length = len(message)
    send_length = str(length).encode('utf-8')
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode('utf-8'))


if __name__ == '__main__':
    usuario = User("user", "password", 19)
    print(f'Sended: {usuario.__str__()}')
    send_obj(usuario)
