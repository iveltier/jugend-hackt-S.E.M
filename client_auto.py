import socket

SERVER_IP = "192.168.172.216"
PORT = 12345

def main():
    print("Client startet")
    
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((SERVER_IP, PORT))
            print(f"Verbunden mit Server {SERVER_IP}:{PORT}")
            
            while TRUE:
                message = input("Nachricht ('exit' zum Beenden):")
                if message.lower() == "exit":
                    break
                
                s.sendall(message)
                
                data = s.recv(1024)
                print(f"Server Antwort: {data}")
                
        except ConnectionRefusedError:
            print("Fehler: Server nicht erreichbar!")
        except Exception as e:
            print(f"Fehler: {e}")
            
if __name__ == "__main__":
    main()