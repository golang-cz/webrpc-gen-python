from flask import Flask, jsonify
from client import ExampleServiceClient

app = Flask(__name__)
client = ExampleServiceClient("http://localhost:8080")

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/ping')
def ping():
    result = client.ping()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

