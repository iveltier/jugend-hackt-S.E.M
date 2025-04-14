import socket

def main():
    SERVER_IP = input ("Input Server-IP: ").strip()
    PORT = 12345

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((SERVER_IP, PORT))
            print("✅ Connected to Server!")
            
            while True:
                message = input("📤 Message ('exit' to exit): ")
                if message.lower() == "exit":
                    break
                s.sendall(message.encode("utf-8"))
                data = s.recv(1024)
                print(f"📥 Server-Answer: {data.decode('utf-8')}")
    
    except ConnectionRefusedError:
        print("❌ Cant connect to Server. Is the Server running? IP/Port correct? Are you in the same Wlan?")
    except Exception as e:
        print(f"🔴 Error: {e}")

if __name__ == "__main__":
    main()
