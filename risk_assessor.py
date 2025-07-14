# risk_assessor.py
from models.volatility import VolatilityModel
from models.liquidity import LiquidityModel
from models.governance import GovernanceModel
from models.sentiment import SentimentModel
from models.multifactor import MultiFactorRisk
from models.stress_test import StressTest

class RiskAssessor:
    def __init__(self):
        self.vol_model = VolatilityModel()
        self.liq_model = LiquidityModel()
        self.gov_model = GovernanceModel()
        self.sent_model = SentimentModel()
        self.multi_risk = MultiFactorRisk()
        self.stress_test = StressTest()

    def compute_risk(self, data):
        vol_forecast = self.vol_model.forecast()
        liq_forecast = self.liq_model.forecast()
        gov_prob = self.gov_model.predict(data['gov_features'])
        sent_scores = self.sent_model.analyze(data['tweets'])

        tech_risk = 0.6  # placeholder
        gov_risk = 1 - gov_prob.mean()
        market_risk = vol_forecast.mean()
        liquidity_risk = 1 - liq_forecast['yhat'].mean()/1000000

        multifactor_score = self.multi_risk.compute(tech_risk, gov_risk, market_risk, liquidity_risk)
        return min(max(multifactor_score * 100, 0), 100)), 100)