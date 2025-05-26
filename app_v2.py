from flask import Flask, jsonify
import time

app = Flask(__name__)
request_count = 0  # Счетчик запросов

@app.route('/time')
def get_time():
    global request_count
    request_count += 1
    return jsonify({"time": int(time.time())})

@app.route('/metrics')
def get_metrics():
    return jsonify({"count": request_count})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
