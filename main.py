#!/bin/bash/python3

# We could probably just use sockets but for ease of use we will use flask to serve, and since the requirements
# require json interaction we will import jsonify as well
from flask import Flask
from flask import jsonify

# Instatiate flask server
app = Flask(__name__)

# Set up one endpoint
@app.route('/')
def hello_world():
    # Return JSON body
    return jsonify(body='Land')

# Final PUT endpoint
@app.route('/', methods=['PUT'])
def string_flip():
    put_input = request.args.get('input')
    # Reverse using slicing
    body_output = put_input[::-1]
    # Return reversed string
    return jsonify(body=body_output), 200

# Run Code
if __name__ == '__main__':
    app.run()
