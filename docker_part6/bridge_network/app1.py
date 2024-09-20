from flask import Flask ,jsonify
import requests

app = Flask(__name__)

@app.route(/app1)

def get_the_req_from_app_2():
    resp = requests.get('http:')