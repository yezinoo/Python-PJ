import socket
import threading

clients =[]

def handle_client(conn,addr):
    print(f"New connection by {addr}")
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            message = f"{addr}: {data.decode()}"
            print(f"{addr}", data.decode())
            for client in clients:
                if client != conn:
                    client.sendall(message.encode())
        except:
            break
    print(f"Diconnected: {addr}")
    clients.remove(conn)
    conn.close()
def start_serer():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 8080))
    server.listen()
    print("Server is listening on port 8080...")
    while True:
        conn, addr = server.accept()
        #print(f"Connected by {addr}")
        clients.append(conn)
        threat = threading.Thread(target=handle_client,args=(conn,addr))
        threat.start()


if __name__=="__main__":
    start_serer()