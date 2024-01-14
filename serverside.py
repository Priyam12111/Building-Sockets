import socket

HOST = '0.0.0.0'  # Replace with ngrok public URL when using ngrok
PORT = 8181
print("Checking New Connection...")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print('Received:', data.decode())
            conn.sendall(data)  # Echo back the message
