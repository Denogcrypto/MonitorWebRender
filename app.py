from flask import Flask, jsonify
import requests
import time

app = Flask(__name__)

URL = "https://portafolioconagentia.vercel.app/"

@app.route("/metrics")
def metrics():
    try:
        start = time.time()
        r = requests.get(URL, timeout=5)
        latency = round((time.time() - start) * 1000)

        return jsonify({
            "status": "UP" if r.status_code == 200 else "DOWN",
            "latency": latency,
            "code": r.status_code
        })

    except Exception as e:
        return jsonify({
            "status": "DOWN",
            "error": str(e)
        })

@app.route("/")
def dashboard():
    return open("index.html").read()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
