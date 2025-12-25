#!/usr/bin/env python3

import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from joblib import dump
import os

DATA_FILE = "sensor_data.csv"
MODEL_FILE = "isoforest_global.joblib"
SCALER_FILE = "scaler.joblib"

print("[TRAIN] Loading dataset...")

if not os.path.exists(DATA_FILE):
    raise FileNotFoundError("sensor_data.csv not found. Run collector first.")

df = pd.read_csv(DATA_FILE)

# Remove rows with missing or corrupted data
df = df.dropna(subset=["temperature", "humidity", "motion"])
df = df[(df["temperature"] > -20) & (df["temperature"] < 80)]  # realistic range
df = df[(df["humidity"] > 0) & (df["humidity"] <= 100)]        # humidity 0-100%

print(f"[TRAIN] Training on {len(df)} rows")

X = df[["temperature", "humidity", "motion"]].values

# Normalize the data (important when mixing different devices)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Save scaler
dump(scaler, SCALER_FILE)
print("[TRAIN] Scaler saved")

# Train IsolationForest
model = IsolationForest(
    n_estimators=300,
    contamination=0.03,   # 3% anomalies expected
    random_state=42
)
model.fit(X_scaled)

dump(model, MODEL_FILE)

print("[TRAIN] Training complete. Model saved.")

