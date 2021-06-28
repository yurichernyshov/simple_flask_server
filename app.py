from flask import Flask, jsonify
import os
from sys import argv


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello from Flask"


@app.route("/api/get_sample/cpu")
def get_sample_cpu():

    process = os.popen('cat /proc/loadavg | awk \'{print $1}\'')
    cpu_usage  = process.read()
    process.close()

    return jsonify({"sample": cpu_usage})


@app.route("/api/get_sample/double/<int:sample>")
def predict(sample):

    return jsonify({"prediction": sample*2})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=argv[1], debug=True)

