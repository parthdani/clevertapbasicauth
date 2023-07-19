from flask import Flask, request, jsonify
import base64
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='log.txt', level=logging.INFO)

# API endpoint
@app.route('/api/endpoint', methods=['POST'])
def api_endpoint():
    auth = request.headers.get('Authorization')

    # Check if Basic authentication is provided
    if not auth or not auth.startswith('Basic '):
        return jsonify({'message': 'Unauthorized'}), 401

    # Extract the username and password from the Basic auth header
    credentials = base64.b64decode(auth.split(' ')[1]).decode().split(':')
    username = credentials[0]
    password = credentials[1]

    # Check if the username and password match
    if username == 'parth_clevertap_auth' and password == 'CleverTap@12_Auth':
        # Authentication successful
        logging.info(str(request.json))
        return jsonify({'message': 'OK'}), 200
    else:
        # Authentication failed
        return jsonify({'message': 'Unauthorized'}), 401

# Start the server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
