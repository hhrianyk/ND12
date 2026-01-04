print("Server Started")

from socket import *
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(("localhost",12345))
server_socket.listen(255)
server_socket.setblocking(False)


clients = []
while True:
    # Підключення до сервера нового клієнта
    try:
        connection, address = server_socket.accept()

        client_name = connection.recv(1024).decode()
        print(f"Відбулось підключення: Клієнт {client_name} {address}")
        connection.send("Вітаємо на нашому сервері LogiTalk".encode())
        connection.setblocking(False)

        for c in clients:
            c[0].send(f"{client_name}: - доєднався до чату".encode())

        clients.append([connection, client_name])

    except BlockingIOError:
        pass
    # Розсилака повідомлень
    for client in clients:
        try:
            message = client[0].recv(1024).decode().strip()

            for c in clients:
                print()
                if client != c:
                    c[0].send(f"{client[1]}: {message}".encode())
        except BlockingIOError:
            pass
        except :
            for c in clients:
                if client != c:
                    c[0].send(f"{client[1]}: - покинув чат")

            client[0].close()
            clients.remove(client)

