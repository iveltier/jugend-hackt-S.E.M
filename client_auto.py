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
                # message.lower
                #encode
                s.sendall(coden(message.lower()))
                data = s.recv(1024)
                #decode
                data = entcoden(data)
                display.set_text_upper(f"{data}")
    
    except ConnectionRefusedError:
        display.set_text_upper(" Server nicht erreichbar. Ist er gestartet? IP/Port korrekt?")
    except Exception as e:
        display.set_text_upper(f" Fehler: {e}")

if __name__ == "__main__":
    main()

