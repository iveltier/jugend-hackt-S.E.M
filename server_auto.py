import socket

HOST = '192.168.172.217'
PORT = 12345

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"🟢 Server läuft auf {HOST}:{PORT}")
        
        conn, addr = s.accept()
        with conn:
            print(f"🔗 Verbunden mit {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"📥 Empfangen: {data.decode('utf-8')}")
                reply = input("📤 Antwort ('exit' zum Beenden): ")
                if reply.lower() == 'exit':
                    break
                conn.sendall(reply.encode('utf-8'))

if __name__ == "__main__":
    main()