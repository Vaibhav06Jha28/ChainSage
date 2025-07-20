import os
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from sklearn.ensemble import IsolationForest
from sklearn.datasets import make_blobs
import pandas as pd
import joblib
import gym
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
import numpy as np

# Temporary patch for numpy >= 1.25
if not hasattr(np, 'bool8'):
    np.bool8 = np.bool_


# Create directory
os.makedirs("models/codebert_classifier", exist_ok=True)

# Load CodeBERT (GPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = AutoModelForSequenceClassification.from_pretrained(
    "microsoft/codebert-base",
    num_labels=2,
    use_safetensors=True
).to(device)

tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base")
model.save_pretrained("models/codebert_classifier")
tokenizer.save_pretrained("models/codebert_classifier")
print("✅ CodeBERT saved.")

# Train Isolation Forest
X, _ = make_blobs(n_samples=300, centers=1, n_features=4, random_state=42)
df = pd.DataFrame(X, columns=["amount", "gas", "input_entropy", "delay"])
clf = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
clf.fit(df)
joblib.dump(clf, "models/isolation_forest.pkl")
print("✅ Isolation Forest saved.")

# Train PPO wallet RL model
env = DummyVecEnv([lambda: gym.make("CartPole-v1")])
ppo_model = PPO("MlpPolicy", env, verbose=1, device="cuda" if torch.cuda.is_available() else "cpu")
ppo_model.learn(total_timesteps=10000)
ppo_model.save("models/ppo_wallet")
print("✅ PPO agent saved as models/ppo_wallet.zip")
