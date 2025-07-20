# ai_models/rl_wallet_monitor.py

import os
import gym
from stable_baselines3 import PPO

class WalletMonitorAgent:
    def __init__(self, env_path="CartPole-v1", model_path=None):
        if model_path is None:
            model_path = os.path.join("models", "ppo_wallet.zip")
        self.env = gym.make(env_path)
        self.model = PPO.load(model_path)

    def act(self, state):
        action, _ = self.model.predict(state)
        return action
