# Jugend hackt - S.E.M.

### S.E.M. (Sender-Empfänger-Modul)

## Projektbeschreibung

Erstelle und programmiere zwei Raspberry Pi 5s, um Nachrichten zwischen ihnen zu senden.

- Erstelle ein 3D-Modell des Raspberry Pi 5 

- Designe eine Box und baue sie mit einem Lasercutter 

- Programmiere ein Programm zur Datenübertragung

- Verbinde beide Raspberry Pi 5s im selben Netzwerk

- Sende Nachrichten

# Verwendung

#### Benötigte Materialien

- 2x Raspberry Pi 5 (nur auf RPi5 getestet, sollte aber auch auf anderen funktionieren)

- WLAN-Verbindung

- Eingabegeräte für beide Raspberry Pis + Monitor + Stromkabel + WLAN-Adapter (falls erforderlich)

1. Einrichten der Raspberry Pis

- Installiere Raspberry Pi OS mithilfe des [Raspberry PI Imager](https://www.raspberrypi.com/software/) und befolge die Anweisungen auf dem Bildschirm
- Führe folgende Befehle aus:

```sudo apt update &&
sudo apt upgrade &&
sudo apt install python && sudo apt install git
```

#### 2. Repository klonen

- Führe den folgenden Befehl aus:

```
git clone https://github.com/iveltier/jugend-hackt-S.E.M
```

- Wechsle in das neue Verzeichnis:

```
cd jugend-hackt-S.E.M.
```

#### 3. Optional: Erstelle ein eigenes lokales WLAN

- Wenn du beide Geräte in ein eigenes WLAN bringen möchtest, führe aus:

```
./createHotspot.sh <hotspot name> <hotspot password>
```

Andernfalls kannst du einfach fortfahren.

#### 4. Server auf der Server-Seite erstellen

- Wähle einen Raspberry Pi 5 als Server aus.
- Führe auf der Server-Seite aus:

```
./createServer.sh
```

Der Server sollte jetzt laufen und auf den Client warten:

```
Server-IP: 192.168.1.1
Waiting for client...
```

#### 5. Client auf der Client-Seite erstellen

- Führe auf dem anderen Raspberry Pi 5 aus:

```
./createClient.sh
```

- Gib die IP-Adresse der Server-Seite ein:

```
Input server-IP:
```

Wenn alles korrekt eingerichtet ist, solltest du nun in der Lage sein, Nachrichten abwechselnd zu senden.

- Server-Seite:

```
Server-IP: 192.168.1.205
Waiting for client...
Client 192.168.1.205 connected!
📥 Client: hello world
📤 Answer: bye world
```

- Client-Seite:

```
Input Server-IP: 192.168.1.205
✅ Connected to Server!
📤 Message ('exit' to exit): hello world
📥 Server-Answer: bye world
📤 Message ('exit' to exit): exit
```

## Name der Teilnehmer\*innen

- Theodor, Phillip, Tillmann, Levi, Lukas, Johnathan, Constantin

## Name der Mentor\*innen

- Anna, Timo, Kostia
