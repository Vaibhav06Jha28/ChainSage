# ai_models/fraud_anomaly_model.py

from sklearn.ensemble import IsolationForest
import pandas as pd
import joblib
import os

class FraudAnomalyDetector:
    def __init__(self, model_path=None):
        if model_path is None:
            model_path = os.path.join("models", "isolation_forest.pkl")
        self.model = joblib.load(model_path)

    def detect(self, features: pd.DataFrame):
        return self.model.predict(features)  # -1 = anomaly, 1 = normal
