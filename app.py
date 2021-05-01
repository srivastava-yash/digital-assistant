import flask
from flask import jsonify, request

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Digital Assistant</h1><p>This is an API which classifies the intent for our digital assistant</p>", 200

#sample url to call - http://127.0.0.1:5000/jarvis?str=give+me+the+details+of+shiv+dutt
@app.route('/jarvis', methods=['GET'])
def jarvis():
    args = request.args
    str = ""
    if "str" in args:
        str = args.get("str")
    if str != "":
        input = str.split("+")
        input = " ".join(input)
    print(input)
    #yaha pe apna model wala function call kardenge phir json ya jo bhi return mardenge
    return "<h1>Json lelo</h1>", 200

# server running on port 5000
app.run()