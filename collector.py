#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import json, time, csv, os

DATA_FILE = "sensor_data.csv"

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "device", "temperature", "humidity", "motion"])


def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())

    # default missing keys to None
    temp = data.get("temperature")
    hum = data.get("humidity")
    motion = data.get("motion")

    with open(DATA_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([time.time(), data["device"], temp, hum, motion])
    print("Saved:", data)


client = mqtt.Client()
client.connect("localhost", 1883, 60)
client.subscribe("devices/data")
client.on_message = on_message
print("Collector Started - Waiting for data ...")
client.loop_forever()
