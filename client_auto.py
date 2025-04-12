import socket

def main():
    SERVER_IP = input ("Server-IP eingeben: ").strip()
    PORT = 12345

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((SERVER_IP, PORT))
            print("✅ Verbunden mit Server!")
            
            while True:
                message = input("📤 Nachricht ('exit' zum Beenden): ")
                if message.lower() == "exit":
                    break
                s.sendall(message.encode("utf-8"))
                data = s.recv(1024)
                print(f"📥 Server-Antwort: {data.decode('utf-8')}")
    
    except ConnectionRefusedError:
        print("❌ Server nicht erreichbar. Ist er gestartet? IP/Port korrekt?")
    except Exception as e:
        print(f"🔴 Fehler: {e}")

if __name__ == "__main__":
    main()
