from flask import Flask, render_template, request
from data_fetcher import DataFetcher
from tasks import monitor_protocol
from socket_events import socketio

app = Flask(__name__)
socketio.init_app(app)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        network = request.form['network']
        addresses = request.form['protocol_addresses'].split(',')
        monitor_protocol.delay(network, addresses)  # async task
        return render_template('index.html', submitted=True)
    return render_template('index.html', submitted=False)

if __name__ == '__main__':
    socketio.run(app, debug=True)