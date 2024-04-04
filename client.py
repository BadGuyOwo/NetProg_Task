import socket

# إعداد العنوان والمنفذ
host = '127.0.0.1'
port = 12345

# إنشاء كائن socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# الاتصال بالخادم
client_socket.connect((host, port))

while True:
    # إرسال البيانات إلى الخادم
    message = input("Enter message to send: ")
    client_socket.sendall(message.encode())

    # استقبال الرد من الخادم
    response = client_socket.recv(1024)
    print("Server response:", response.decode())

# إغلاق الاتصال
client_socket.close()
