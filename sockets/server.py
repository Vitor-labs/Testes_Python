
import time
import socket
import threading

PORT = 5050
HEADER = 64
SERVER = socket.gethostbyname(socket.gethostname())
SERVER_ADDRESS = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(SERVER_ADDRESS)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    while True:
        request = conn.recv(HEADER).decode("utf-8")
        if request:
            length = int(request)
            message = conn.recv(length).decode("utf-8")
            if message == "!DISCONNECT":
                print(f"[DISCONNECT] {addr} disconnected.")
                conn.close()
                break
            print(f"[{addr}] {message}")
            conn.send(f"Message received".encode("utf-8"))
            response = bytes("Hello from the other side", "utf-8")
            conn.send(response)

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER_ADDRESS}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] Server is starting...")
start()
