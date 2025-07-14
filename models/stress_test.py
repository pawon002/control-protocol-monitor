# models/stress_test.py
import numpy as np

class StressTest:
    def simulate_shocks(self, returns, shock_percent=0.1):
        shocked = returns.copy() * (1 - shock_percent)
        return shocked.describe()