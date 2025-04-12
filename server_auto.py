import socket

HOST = '0.0.0.0'
PORT = 12345

def main():
    print("Server startet automatisch...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("Server läuft auf {HOST}:{PORT}. Warte auf Client...")
        
        conn, addr = s.addr = s.accept()
        with conn:
            print(f"Verbunden mit {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    print("Client getrennt")
                    break
                print(f"Empfangen: {data}")
                reply = input("Antwort oder 'exit' zum Beenden):")
                if reply.lower() == 'exit':
                    break
                conn.sendall(reply)
                
if __name__ == "__main__":
    main()