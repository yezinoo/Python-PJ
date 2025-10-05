import socket
import threading
def send_message(sock):
    while True:
        try:
            data= sock.recv(1024)
            if not data:
                break
            print("\n" + data.decode() + "\nYou: ", end="")
        except:
            break

def start_client():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(("127.0.0.1",8080))
    print("Connected to server. Type Message:")
    thread = threading.Thread(target=send_message,args=(client,))
    thread.daemon=True
    thread.start()
    while True:
        msg = input("You: ")
        client.sendall(msg.encode())

if __name__=="__main__":
    start_client()
