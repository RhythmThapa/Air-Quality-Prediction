"""Command-line predictor for CO(GT) concentration."""
import json
from pathlib import Path

import joblib
import numpy as np

MODELS_DIR = Path(__file__).resolve().parent / "models"

model = joblib.load(MODELS_DIR / "air_quality_model.joblib")
scaler = joblib.load(MODELS_DIR / "scaler.joblib")
with open(MODELS_DIR / "feature_names.json") as f:
    features = json.load(f)

print("\nAIR QUALITY PREDICTION")
print("-" * 35)

values = [float(input(f"Enter {name}: ")) for name in features]

data = np.array(values).reshape(1, -1)
prediction = model.predict(scaler.transform(data))[0]

print(f"\nPredicted CO(GT): {prediction:.4f}")
