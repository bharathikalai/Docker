from flask import Flask , jsonify
import requests

app = Flask(__name__)

@app.route('/app1')

def get_req_from_second_application():
    resp = requests.get('http://172.19.0.3:5000/app2')
    return jsonify(resp.json())

if __name__ == "__main__":
    app.run(host = '0.0.0.0',port=5000)