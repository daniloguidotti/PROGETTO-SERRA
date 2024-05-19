import socket
import threading

# Словарь для хранения подключенных клиентов
clients = {}

# Функция для обработки сообщений от клиента
def handle_client(client_socket, player_id):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            process_message(message, player_id)
        except:
            del clients[player_id]
            client_socket.close()
            break

# Функция для обработки сообщений
def process_message(message, player_id):
    print(f"{player_id} says: {message}")
    # Здесь будет добавлена логика обработки выстрелов и обновлений игры

# Функция для рассылки сообщений всем клиентам
def broadcast(message):
    for client in clients.values():
        client.send(message.encode('utf-8'))

# Настройка сервера
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5555))
server.listen(2)

print("Server started, waiting for connections...")

# Подключение двух игроков
for player_id in ['player1', 'player2']:
    client_socket, addr = server.accept()
    clients[player_id] = client_socket
    print(f"New connection from {addr} as {player_id}")
    client_handler = threading.Thread(target=handle_client, args=(client_socket, player_id))
    client_handler.start()
