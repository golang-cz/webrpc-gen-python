from flask import Flask, request, jsonify
from client import ExampleService, PingArgs, GetUserArgs, User, Kind  # import necessary classes from your generated code

app = Flask(__name__)

service = ExampleService('http://localhost:5000')  # initialise the service with the localhost URL


@app.route('/rpc/helloworld')
def hello_world():
    return 'Hello, World!'

@app.route('/rpc/ExampleService/Ping')
def ping():
    args = PingArgs()  # Create an empty PingArgs instance if no input is required
    response = service.Ping(args)  # Call the service method
    return jsonify(response.to_dict())


@app.route('/rpc/ExampleService/GetUser', methods=['GET'])
def get_user():
    user_id = request.args.get('userID')
    if user_id is None:
        return jsonify({"error": "Missing userID query parameter"}), 400
    try:
        user_id = int(user_id)
    except ValueError:
        return jsonify({"error": "userID must be an integer"}), 400
    args = GetUserArgs(userID=user_id)
    response = service.GetUser(args)
    return jsonify(response.to_dict())


if __name__ == '__main__':
    app.run(debug=True)  # Start the Flask application
