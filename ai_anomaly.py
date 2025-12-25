#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import pandas as pd
import json
import time
import os
from sklearn.preprocessing import StandardScaler
from joblib import load
import RPi.GPIO as GPIO 

BUZZER_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

DATA_FILE = "sensor_data.csv"
MODEL_FILE = "isoforest_global.joblib"
SCALER_FILE = "scaler.joblib"

BROKER = "192.168.43.56"
TOPIC_DATA = "devices/data"
TOPIC_ALERT = "alerts/anomaly"

# Load model + scaler
if not os.path.exists(MODEL_FILE) or not os.path.exists(SCALER_FILE):
    raise FileNotFoundError("Model or scaler missing. Run trainer.py first.")

model = load(MODEL_FILE)
scaler = load(SCALER_FILE)

RED = "\033[91m"
BLINK = "\033[5m"
RESET = "\033[0m"
BOLD = "\033[1m"


def terminal_alert(message):
    print("\a")
    print(f"{BLINK}{RED}{BOLD}[ANOMALY ALERT]{RESET} {message}")
    # ---- Activate buzzer for 1 second ----
    GPIO.output(BUZZER_PIN, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(BUZZER_PIN, GPIO.LOW)


def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker")
    client.subscribe(TOPIC_DATA)


def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())
    except:
        print("Invalid JSON received.")
        return

    device = data.get("device", "unknown")

    try:
        temp = float(data.get("temperature", 0))
        hum = float(data.get("humidity", 0))
        motion = float(data.get("motion", 0))
    except ValueError:
        print("Corrupt sensor data, ignored.")
        return

    # Log the data
    df_new = pd.DataFrame(
        [[time.time(), device, temp, hum, motion]],
        columns=["timestamp", "device", "temperature", "humidity", "motion"],
    )
    df_new.to_csv(DATA_FILE, mode="a", header=False, index=False)

    # Prepare for prediction
    X = [[temp, hum, motion]]
    X_scaled = scaler.transform(X)

    prediction = model.predict(X_scaled)[0]

    if prediction == -1:
        alert_msg = f"Device={device}, Temp={temp:.2f}, Hum={hum:.2f}, Motion={motion}"
        terminal_alert(alert_msg)
        client.publish(TOPIC_ALERT, alert_msg)
    else:
        print(f"OK [{device}] T={temp:.1f} H={hum:.1f} M={motion}")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

print("Starting AI anomaly detector...")
client.connect(BROKER, 1883, 60)
try:
    client.loop_forever()
finally:
    GPIO.cleanup() 

