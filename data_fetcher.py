# data_fetcher.py
import requests
import pandas as pd
from config import *

class DataFetcher:
    def fetch_blockchain_events(self, network: str, addresses: list):
        # TODO: switch on network and call appropriate scan API
        pass

    def fetch_market_data(self, symbol: str, vs_currency: str = 'usd') -> pd.DataFrame:
        # Example: CoinGecko price history
        url = f"{COINGECKO_URL}/coins/{symbol}/market_chart"
        params = {'vs_currency': vs_currency, 'days': 30}
        r = requests.get(url, params=params)
        data = r.json()
        return pd.DataFrame(data['prices'], columns=['timestamp','price'])

    def fetch_social_sentiment(self, query: str) -> pd.DataFrame:
        # TODO: Twitter API v2 search, return tweets and basic sentiment
        pass

    def fetch_governance_votes(self, proposal_id: str) -> pd.DataFrame:
        # TODO: call Snapshot or Tally endpoints
        pass