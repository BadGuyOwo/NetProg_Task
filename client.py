import socket

host = '127.0.0.1'
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((host, port))

while True:
    message = input("Enter message to send: ")
    client_socket.sendall(message.encode())

    response = client_socket.recv(1024)
    print("Server response:", response.decode())

client_socket.close()
