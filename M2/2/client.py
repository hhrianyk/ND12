print("Client Started")

from socket import *
client_socket = socket(AF_INET, SOCK_STREAM)
name = input("Enter your name: ")
client_socket.connect(("localhost",12345))
client_socket.send(name.encode())
print(client_socket.recv(1024).decode())

print("Що ти хочеш зробити:")
print("NAME - ваше імя у базі")
print("EXIT - завершити підключення")
ans = input("Що ти хочеш зробити:")
client_socket.send(ans.encode())
print(client_socket.recv(1024).decode())
client_socket.close()

