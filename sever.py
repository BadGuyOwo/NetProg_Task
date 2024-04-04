import  socket

# إعداد العنوان والمنفذ
host = '127.0.0.1'
port = 12345

# إنشاء كائن socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ربط العنوان والمنفذ بالكائن socket
server_socket.bind((host, port))

# الاستماع للاتصالات الواردة
server_socket.listen(5)

print("Waiting for client connection...")

# قبول اتصال العميل
client_socket, addr = server_socket.accept()
print('Connected to', addr)

while True:
    # استقبال البيانات من العميل
    data = client_socket.recv(1024)
    if not data:
        break
    print("Received message:", data.decode())

    # إرسال رد إلى العميل
    client_socket.sendall(b"Message received!")

# إغلاق الاتصال
client_socket.close()
server_socket.close()
