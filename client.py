import socket

HOST = '0.tcp.in.ngrok.io'  # Replace with ngrok public URL when using ngrok
PORT = 19264

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    message = input('Enter message: ')
    s.sendall(message.encode())
    data = s.recv(1024)
    print('Received:', data.decode())
