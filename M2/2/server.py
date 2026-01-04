print("Server Started")

from socket import *
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(("localhost",12345))
server_socket.listen(1)

connection, address = server_socket.accept()


client_name = connection.recv(1024).decode()
print(f"Відбулось підключення: Клієнт {client_name} {address}")
connection.send("Вітаємо на нашому сервері LogiTalk".encode())

command = connection.recv(1024).decode()
if command == "NAME":
    connection.send(f"Клієнт {client_name} {address}".encode())
elif command == "EXIT":
    connection.send(f"Гарного тобі дня".encode())
    connection.close()
else:
    connection.send(f"Такої команди нема".encode())
server_socket.close()

