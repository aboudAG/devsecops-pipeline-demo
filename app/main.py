from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.get("/add/<int:a>/<int:b>")
def add(a, b):
    return jsonify({"a": a, "b": b, "result": a + b}), 200
