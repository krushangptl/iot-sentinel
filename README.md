# IoT-Sentinel

## AI-Powered Network Anomaly Detector

**AIM:**
AI-Powered IoT Network Anomaly Detector, uses a Raspberry Pi as both the central IoT gateway and AI engine to monitor network traffic from simulated IoT devices.
Multiple Python scripts running on the Pi act as virtual IoT nodes, publishing sensor-like data (temperature, humidity, etc.) over the MQTT(Message Queuing Telemetry Transport) protocol to a broker hosted on the Pi.
The Pi collects this data along with network metadata such as packet size, frequency, and device ID, then applies an AI anomaly detection model trained on normal traffic patterns.
If unusual traffic is detected—such as abnormally high frequency or oversized packets—the system flags it as an anomaly and triggers an alert, demonstrating how AI can enhance IoT network security.
