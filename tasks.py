from celery import Celery
from data_fetcher import DataFetcher
from risk_assessor import RiskAssessor
from socket_events import socketio

celery = Celery('tasks', broker='redis://localhost:6379/0')
fetcher = DataFetcher()
assessor = RiskAssessor()

@celery.task
def monitor_protocol(network, addresses):
    events = fetcher.fetch_blockchain_events(network, addresses)
    market_data = fetcher.fetch_market_data(network.lower())
    tweets = fetcher.fetch_social_sentiment(network)
    gov = fetcher.fetch_governance_votes('')

    data = {
        'returns': market_data['price'].pct_change().dropna(),
        'gov_features': gov,
        'tweets': tweets['text'].tolist()
    }

    score = assessor.compute_risk(data)
    socketio.emit('risk_update', {'network': network, 'risk': round(score, 2)})
    return score