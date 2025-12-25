#!/usr/bin/env python3
import paho.mqtt.publish as publish
import psutil, time, json, socket, random

BROKER = "192.168.43.56"
TOPIC = "devices/data"
DEVICE = socket.gethostname()

counter = 0
while counter <= 1000:
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent

    data = {
        "device": DEVICE,
        "temperature": 25 + (cpu / 10.0),  # mild fluctuation
        "humidity": 50 + (mem / 10.0),
        "motion": random.choice([0, 1]),  # 0 = no motion, 1 = motion
    }

    publish.single(TOPIC, json.dumps(data), hostname=BROKER)
    print("Published (Normal):", data)
    counter += 1
    time.sleep(2)
