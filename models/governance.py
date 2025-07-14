
# models/governance.py
import joblib, os

class GovernanceModel:
    def __init__(self):
        self.clf = joblib.load(os.path.join("models","pretrained","rf_governance_model.joblib"))

    def predict(self, X):
        return self.clf.predict_proba(X)[:,1]
