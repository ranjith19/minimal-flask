from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/status")
def hello_world():
    return jsonify(dict(status=True))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="3991")
