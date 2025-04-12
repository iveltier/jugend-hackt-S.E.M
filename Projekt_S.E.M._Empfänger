Antwort = input()
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
    print (Zeichen)

    #print ("zeichen=", Zeichen)
    
    #print (Zeichen_Index)
    
    #print (neues_Zeichen)
   
    #print (Zahl)
    #print (neue_Zahl)
    x = x+1

