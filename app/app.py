from flask import Flask, jsonify
import socket
import time
import random

app = Flask(__name__)

@app.route("/status")
def hello_world():
    print(f"hostname :{socket.gethostname()}")
    time.sleep(random.random())
    return jsonify(dict(status=True, hostname=socket.gethostname()))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="3991")
