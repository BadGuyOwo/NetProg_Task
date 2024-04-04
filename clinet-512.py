import socket
import threading

# Set up the client
host = '127.0.0.1'
port = 12345

client_name = input("Enter your name: ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

# Function to receive messages from the server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(512).decode()
            if message:
                print(message)
        except:
            break

# Start a thread to receive messages from the server
receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

# Main loop to send messages to the server
while True:
    message = input("Enter the message you want to send: ")
    if message.lower() == "quit":
        client_socket.sendall(f"{client_name}: has left the chat".encode())
        break
    else:
        # Send the message
        client_socket.sendall(f"{client_name}: {message}".encode())

# Close the client socket
client_socket.close()
