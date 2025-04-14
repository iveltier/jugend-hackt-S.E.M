import socket

def get_local_ip():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except:
        return "127.0.0.1"

def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 12345))
    s.listen()
    
    ip = get_local_ip()
    print(f"Server-IP: {ip}")
    print("Waiting for client...")  
    
    conn, addr = s.accept()
    print(f"Client {addr[0]} connected!")
    
    while True:
        data = conn.recv(1024).decode()
        if not data: break
        print("📥 Client:", data)
        conn.sendall(input("📤 Answer: ").encode())

if __name__ == "__main__":
    start_server()