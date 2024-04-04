import socket
import threading

# List to keep track of connected clients
clients = []

# Function to handle messages from clients
def handle_client(client_socket, client_addr):
    print(f"Connected: {client_addr}")
    clients.append(client_socket)

    while True:
        try:
            # Receive message from client
            message = b''
            while True:
                chunk = client_socket.recv(512)
                if not chunk:
                    break
                message += chunk
                if len(chunk) < 512:
                    break

            if message:
                # Print the message
                message_decoded = message.decode()
                print(message_decoded)

                # Broadcast the message to all other clients
                for client in clients:
                    if client != client_socket:
                        client.sendall(message)
            else:
                # If no message is received, close the connection
                print(f"Client {client_addr} disconnected.")
                client_socket.close()
                clients.remove(client_socket)
                break
        except:
            print(f"Client {client_addr} disconnected unexpectedly.")
            client_socket.close()
            clients.remove(client_socket)
            break

# Set up the server
host = '127.0.0.1'
port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)

print("Server is ready and waiting for clients...")

# Accept and handle client connections
while True:
    client_socket, client_addr = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_addr))
    client_thread.start()
