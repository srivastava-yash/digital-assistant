import flask
from flask import jsonify, request

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Assistant</h1><p>This is an API which classifies the intent for our digital assistant</p>"

#sample url to call - http://127.0.0.1:5000/jarvis?input=give+me+the+details+of+shiv+dutt
@app.route('/jarvis', methods=['GET'])
def jarvis():
    #yaha pe apna model wala function phir json ya jo bhi return mardenge
    #return jsonify()
    return "<h1>Json lelo</h1>"

# server running on port 5000
app.run()