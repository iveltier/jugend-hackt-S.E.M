Antwort = input()
Naricht = list( Antwort.split())  #Geben Sie die Naricht ein. Trenne Buchstaben und Zeichen durch leerzeichen
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
    print (neue_Zahl)
    x = x+1

