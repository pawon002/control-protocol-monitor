# models/volatility.py
import joblib, os

class VolatilityModel:
    def __init__(self):
        path = os.path.join("models", "pretrained", "garch_ethereum.joblib")
        self.model = joblib.load(path)

    def forecast(self, horizon: int = 5):
        return self.model.forecast(horizon=horizon).variance.iloc[-1]