from fastapi import APIRouter
from pydantic import BaseModel
import pandas as pd
import os
from ai_models.fraud_anomaly_model import FraudAnomalyDetector

router = APIRouter()

# Dynamically resolve absolute model path
model_path = os.path.join("models", "isolation_forest.pkl")
model = FraudAnomalyDetector(model_path=model_path)

class AnomalyRequest(BaseModel):
    data: dict  # Example: {"feature1": 0.1, "feature2": 1.2, ...}

@router.post("/detect")
def detect_anomaly(req: AnomalyRequest):
    df = pd.DataFrame([req.data])
    prediction = model.detect(df)[0]  # Returns -1 (anomaly) or 1 (normal)
    label = "Anomaly" if prediction == -1 else "Normal"
    return {"prediction": label}
