# jugend hackt dresden 2025 : S.E.M.

### S.E.M (Sender-Empfänger Modul)

## Projektdescription

Build and program two Raspberry Pi 5s and send messages between them.

- make a 3d modell of RPi5
- desgin box and build with laser cutter
- code transfer data program
- connect both RPi5 in same network
- send messages

# how to use

#### supplies

- 2x RPi 5 (only tested on RPi5, but should work on other ones too)
- wlan connection
- input devices for both RPi's + power supply cable + wlan adapter (if needed)

#### 1. setup RPi's

- install Raspberry Pi OS using [Raspberry PI Imager](https://www.raspberrypi.com/software/) and just follow the instructions on the screen

- run

```sudo apt update &&
sudo apt upgrade &&
sudo apt install python && sudo apt install git
```

#### 2. clone the repo

- run

```
git clone https://github.com/iveltier/jugend-hackt-S.E.M
```

- go to the new dir

```
cd jugend-hackt-S.E.M.
```

#### 3. optional (bc its cool): create own local wifi

- if you want to have both in there own wlan
  run

```
./createHotspot.sh <hotspot name> <hotspot password>
```

else you can just continue

#### 4. create Server on server Side

- choose one RPi5 to be the server
- run on the server side

```
./createServer.sh
```

the server should now be running and waiting for client

```
Server-IP: 192.168.1.1
Waiting for client...
```

#### 5. create Client on client side

- run on the other RPi5

```
./createClient.sh
```

- now you will have to pass the server side ip adress

```
Input server-IP:
```

if done correct, you should now be able to send messages alternately

- server side:

```
Server-IP: 192.168.1.205
Waiting for client...
Client 192.168.1.205 connected!
📥 Client: hello world
📤 Answer: bye world
```

- client side:

```
Input Server-IP: 192.168.1.205
✅ Connected to Server!
📤 Message ('exit' to exit): hello world
📥 Server-Answer: bye world
📤 Message ('exit' to exit): exit
```

## Name of participants

- Theodor, Phillip, Tillmann, Levi, Lukas, Johnathan, Constantin

## Name of the accompanying mentor

- Anna, Timo, Kostia
