import socket
import threading

# Функция для получения сообщений от сервера
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Connection closed")
            client_socket.close()
            break

# Подключение к серверу
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5555))

# Запуск потока для получения сообщений
receive_thread = threading.Thread(target=receive_messages, args=(client,))
receive_thread.start()

# Отправка сообщений на сервер
while True:
    message = input("Enter message: ")
    client.send(message.encode('utf-8'))
