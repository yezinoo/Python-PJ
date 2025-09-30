import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",8080))
print("Connected to server. You can start chatting")
while True:
    msg = input("Client: ")
    client.sendall(msg.encode())
    data = client.recv(1024)
    if not data:
        break
    print("Server:", data.decode())
client.close()
    