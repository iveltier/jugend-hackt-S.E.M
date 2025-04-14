#!/bin/bash

# Überprüfen, ob genügend Argumente übergeben wurden
if [ "$#" -ne 2 ]; then
    echo "Usage: ./createHotspot <hotspot name> <hotspot password>"
    exit 1
fi

# Argumente zuweisen
HOTSPOT_NAME=$1
HOTSPOT_PASSWORD=$2

# Hotspot erstellen
sudo nmcli device wifi hotspot ssid "$HOTSPOT_NAME" password "$HOTSPOT_PASSWORD" ifname wlan0
sudo echo hotspot: $HOTSPOT_NAME created