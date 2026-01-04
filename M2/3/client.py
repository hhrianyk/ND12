print("Client Started")
import threading
from socket import *
client_socket = socket(AF_INET, SOCK_STREAM)
name = input("Enter your name: ")
client_socket.connect(("4.tcp.ngrok.io",19569 ))
client_socket.send(name.encode())
print(client_socket.recv(1024).decode())

def send_message():
    while True:
        message = input()
        client_socket.send(message.encode())

threading.Thread(target=send_message).start()

while True:
    try:
        message = client_socket.recv(1024).decode().strip()
        if message:
            print(message)
    except:
        break

print(client_socket.recv(1024).decode())
client_socket.close()

