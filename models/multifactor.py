# models/multifactor.py
class MultiFactorRisk:
    def compute(self, tech_risk, gov_risk, market_risk, liquidity_risk):
        weights = [0.25, 0.25, 0.25, 0.25]
        return sum([a*b for a, b in zip(weights, [tech_risk, gov_risk, market_risk, liquidity_risk])])