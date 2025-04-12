<<<<<<< HEAD
import socket

SERVER_IP = "192.168.172.217" #server ip eingeben
PORT = 12345

def main():
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
=======
import socket

SERVER_IP = "192.168.1.100"  # Hier Server-IP eintragen!
PORT = 12345

def main():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((SERVER_IP, PORT))
            print("✅ Verbunden mit Server!")
            
            while True:
                message = input("📤 Nachricht ('exit' zum Beenden): ")
                if message.lower() == "exit":
                    break
                s.sendall(message.encode("utf-8"))
                
                data = s.recv(1024).decode("utf-8")
                print(f"📥 Server-Antwort: {data}")
    
    except ConnectionRefusedError:
        print("❌ Server nicht erreichbar. Ist er gestartet? IP/Port korrekt?")
    except Exception as e:
        print(f"🔴 Fehler: {e}")

if __name__ == "__main__":
>>>>>>> b3069d52a8a98b0effc51af1a95029ae1324be78
    main()