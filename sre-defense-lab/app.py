import time
import random
from flask import Flask, jsonify
from prometheus_client import make_wsgi_app, Counter, Histogram
from werkzeug.middleware.dispatcher import DispatcherMiddleware

app = Flask(__name__)

# SRE Metrics: Tracking requests and system speed
REQUEST_COUNT = Counter('mission_requests_total', 'Total mission data packets received', ['status'])
REQUEST_LATENCY = Histogram('mission_request_duration_seconds', 'Time spent processing data packet')

@app.route('/')
def home():
    return jsonify({"status": "ONLINE", "system": "Defense Data Pipeline"})

@app.route('/input', methods=['GET', 'POST'])
def receive_data():
    start_time = time.time()
    try:
        # Simulate normal processing time (random lag between 50ms and 200ms)
        time.sleep(random.uniform(0.05, 0.2)) 
        
        # Artificial Chaos: 10% chance the system drops a packet to simulate an issue
        if random.random() < 0.10:
            REQUEST_COUNT.labels(status='500').inc()
            return jsonify({"status": "ERROR", "message": "Packet dropped"}), 500
            
        REQUEST_COUNT.labels(status='200').inc()
        return jsonify({"status": "SUCCESS", "packet_secured": True}), 200
        
    finally:
        REQUEST_LATENCY.observe(time.time() - start_time)

# Setup Prometheus metrics endpoint
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
