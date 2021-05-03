from argparse import Namespace

import flask
from flask import jsonify
from flask import request
import base64

from predict import predict

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Assistant</h1><p>This is an API which classifies the intent for our digital assistant</p>"

@app.route('/jarvis', methods=['GET'])
def jarvis():
    query = request.args.get('query', type=str)
    if query:
        base64_message = query
        base64_bytes = base64_message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        message = message_bytes.decode('ascii')
        lines = [message.strip().split()]
        args = Namespace(model_dir='./bot_model', batch_size=32, no_cuda=False)
        response = predict(args, lines)
        print(response)
    return jsonify(response)

# server running on port 5000
if __name__=='__main__':
    app.run(host='0.0.0.0')