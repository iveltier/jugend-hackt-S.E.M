import socket
import display



def main():
    SERVER_IP = input ("Server-IP eingeben: ").strip()
    PORT = 12345


    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((SERVER_IP, PORT))
            display.set_text_upper(" Verbunden mit Server!")
            
            
            while True:
                message = input(" Nachricht ('exit' zum Beenden): ")
                if message.lower() == "exit":
                    break
                s.sendall(message)
                data = s.recv(1024)
                display.set_text_upper(f"{data}")
    
    except ConnectionRefusedError:
        display.set_text_upper(" Server nicht erreichbar. Ist er gestartet? IP/Port korrekt?")
    except Exception as e:
        display.set_text_upper(f" Fehler: {e}")

if __name__ == "__main__":
    main()

