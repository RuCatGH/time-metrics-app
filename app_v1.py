from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/time')
def get_time():
    return jsonify({"time": int(time.time())})
