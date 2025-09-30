import socket

server_ip = "0.0.0.0"
server_port = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((server_ip,server_port))
server.listen(1)
print("Server is listening on port 8080...")

conn, addr = server.accept()
print(f"Connected by {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        break
    print("Client",data.decode())
    
    reply = input("Server: ")
    conn.sendall(reply.encode())
conn.close()