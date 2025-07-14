import joblib

class LiquidityModel:
    def __init__(self, model_name='ethereum'):
        self.model = joblib.load(f'models/pretrained/prophet_ethereum.joblib')

    def forecast(self, periods=30):
        future = self.model.make_future_dataframe(periods=periods)
        forecast = self.model.predict(future)
        return forecast[['ds', 'yhat']]  # Predicted TVL