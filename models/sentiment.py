# models/sentiment.py
from transformers import pipeline

class SentimentModel:
    def __init__(self):
        self.nlp = pipeline(
            "text-classification",
            model="ElKulako/cryptobert",
            truncation=True, max_length=128
        )

    def analyze(self, texts: list) -> list:
        return self.nlp(texts)
