# AI-Powered IoT Network Anomaly Detection System

📄 **Project Report (PDF):**  
[AI-Powered IoT Network Anomaly Detection System](./AI-Powered_IoT_Network_Anomaly_Detection_System.pdf)

---

## 1. Introduction

Modern IoT environments generate large volumes of sensor data, making manual detection of abnormal device behavior difficult. Such anomalies may occur due to hardware faults, cyberattacks, spoofed data, or malfunctioning sensors.

This project presents a **real-time IoT anomaly detection system** using a **Raspberry Pi** and an **Isolation Forest machine learning model**. Sensor data is transmitted using the **MQTT protocol** and analyzed at the edge. When an anomaly is detected, the system triggers a buzzer alert, logs the event, and publishes an MQTT alert.

A dataset of **3000 synthetic IoT samples** was used for training, achieving approximately **98% detection accuracy**.

---

## 2. Components Used

### Hardware
- Raspberry Pi 4B  
- GPIO Buzzer  
- Mobile Hotspot  
- Laptop / PC  

### Software
- Python 3  
- MQTT (paho-mqtt)  
- Scikit-learn  
- Joblib  
- Pandas & NumPy  
- RPi.GPIO  

---

## 3. Circuit Design

### Circuit Connections
- Buzzer Positive (+) → GPIO Pin 18  
- Buzzer Negative (–) → Ground (GND)  

The Raspberry Pi runs the anomaly detection script. When abnormal data is detected:
1. The buzzer is activated
2. An alert message is printed on the terminal
3. An MQTT alert is published

---

## 4. System Data Pipeline

### Data Generation
- Synthetic IoT data generated from laptop and Raspberry Pi
- Parameters: temperature, humidity, motion

### Data Collection
- `collector.py` subscribes to `devices/data`
- All incoming data stored in `sensor_data.csv`

### Training Phase
- 3000 data samples used
- Data normalized using `StandardScaler`
- Isolation Forest trained with 98% accuracy

### Real-Time Detection
- Raspberry Pi runs `anomaly_detector.py`
- Incoming data analyzed in real time
- On anomaly:
  - Buzzer activates
  - Terminal alert shown
  - MQTT alert sent to `alerts/anomaly`

---

## 5. Project Files

- `collector.py` – Collects MQTT sensor data  
- `trainer.py` – Trains Isolation Forest model  
- `anomaly_detector.py` – Real-time anomaly detection  
- `device_simulator.py` – Synthetic IoT data generator  
- `buzzer_test.py` – GPIO buzzer test script  

---

## 6. Conclusion

This project demonstrates an effective **AI-based anomaly detection system for IoT networks** using Raspberry Pi and MQTT communication. The trained Isolation Forest model successfully detects abnormal sensor behavior with high accuracy.

The system operates entirely at the edge, provides real-time alerts, and is lightweight, low-cost, and scalable. It is suitable for applications such as smart homes, laboratories, and small industrial environments.

---
