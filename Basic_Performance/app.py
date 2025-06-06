# app.py
from flask import Flask
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time
import random

app = Flask(__name__)

# Prometheus Metrics
REQUEST_COUNT = Counter('app_requests_total', 'Total HTTP requests')
REQUEST_LATENCY = Histogram('app_request_latency_seconds', 'Request latency')

@app.route('/')
def index():
    REQUEST_COUNT.inc()
    with REQUEST_LATENCY.time():
        time.sleep(random.uniform(0.1, 0.5))  # Simulate latency
    return "Hello, performance world!"

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
