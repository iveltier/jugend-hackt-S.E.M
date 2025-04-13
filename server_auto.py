import socket
import display

def coden(Antwort):

    Naricht = "".join(Antwort.split()) #list( Antwort.split())  #Geben Sie die Naricht ein. Trenne Buchstaben und Zeichen durch leerzeichen
    Alphabet = []
    x = 97
    while x < 123:
        Buchstaben = chr(x)
        Alphabet.append(Buchstaben)
        x=x+1
    code = []
    #print (Alphabet)
    x = 0
    output = ''
    Naricht_länge = len(Naricht)
    while x < Naricht_länge:
        Zeichen = Naricht[x]
        #print ("zeichen=", Zeichen)
        Zeichen_Index = Alphabet.index(Zeichen)
        #print (Zeichen_Index)
        neues_Zeichen = Alphabet[(Zeichen_Index + 4)%26]
        #print (neues_Zeichen)
        Zahl = ord(neues_Zeichen)
        #print (Zahl)
        neue_Zahl = Zahl * 2
        #print (neue_Zahl," ",end="")
        output = output + str (neue_Zahl) +" "
        x = x+1
    return output
#result = coden(input())


def entcoden(Antwort):
    Naricht = list(map(int, Antwort.split())) #Geben Sie die Naricht ein. Trenne Buchstaben und Zeichen durch leerzeichen
    Alphabet = []
    x = 97
    while x < 123:
        Buchstaben = chr(x)
        Alphabet.append(Buchstaben)
        x=x+1
    code = []
    #print (Alphabet)
    x = 0
    Naricht_länge = len(Naricht)
    output = ""
    while x < Naricht_länge:
        Zahl = Naricht[x]
        #print (Zahl)
        neue_Zahl = Zahl / 2
        neue_Zahl = int(neue_Zahl)
        neues_Zeichen = chr(neue_Zahl)
        Zeichen_Index = Alphabet.index(neues_Zeichen)
        if Zeichen_Index < 4 :
            Zeichen = Alphabet[(Zeichen_Index - 4+26)%26]
        else:
            Zeichen = Alphabet[(Zeichen_Index - 4)%26]
        #print (Zeichen, end="")
        output = output + Zeichen
        x = x+1
    return output
# result_empfaenger = entcoden(input())

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
    display.set_text_upper(f"Server-IP: {ip}")
    display.set_text_upper("Warte auf Client...")  
    
    conn, addr = s.accept()
    display.set_text_upper(f"Client {addr[0]} verbunden!")
    
    while True:
        data = conn.recv(1024)
        if not data: break
        data = entcoden(data)
        display.set_text_upper(f"{data}")
        conn.sendall(coden(input("Antwort: ")))

if __name__ == "__main__":
    start_server()
