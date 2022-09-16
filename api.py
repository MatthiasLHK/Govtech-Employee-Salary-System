from flask import Flask, request, make_response
from flask_cors import CORS, cross_origin
from flask.helpers import send_from_directory

app = Flask(__name__, static_folder='frontend/build', static_url_path='')
CORS(app)

@app.route('/')
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/test', methods=["GET"])
@cross_origin()
def test():
    return "Hello World"