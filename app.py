from flask import Flask, jsonify
import os
from sys import argv


app = Flask(__name__)


@app.route("/")
def hello():
    message_ = """
    <html>
    <h1>Hello from Flask simple API Server</h1>
    
    <h2>Options:</h2>
    
    <table border=1>
    <tr>
      <th>Команда</th><th>Описание</th>
    </tr>
    <tr>
      <td>/api/get/cpu</td>
      <td>Возвращает значение CPU</td>
    </tr>
    <tr>
      <td>/api/get/double/&lt;int:sample&gt;</td>
      <td>Возврашает удвоенное значение sample</td>
    </tr>
    </table>
    </html>

    """
    return message_


@app.route("/api/get/cpu")
def get_sample_cpu():

    process = os.popen('cat /proc/loadavg | awk \'{print $3}\'')
    cpu_usage  = process.read()
    process.close()

    return jsonify({"sample": cpu_usage[:-1]})


@app.route("/api/get/double/<int:sample>")
def predict(sample):

    return jsonify({"calculation": sample*2})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=argv[1], debug=True)

