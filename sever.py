import  socket

host = '127.0.0.1'
port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((host, port))

server_socket.listen(5)

print("Waiting for client connection...")

client_socket, addr = server_socket.accept()
print('Connected to', addr)

while True:
    data = client_socket.recv(1024)
    if not data:
        break
    print("Received message:", data.decode())

    client_socket.sendall(b"Message received!")

client_socket.close()
server_socket.close()
