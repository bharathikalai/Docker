from flask import Flask , jsonify
import requests

app = Flask(__name__)

@app.route('/app2')

def second_application():
    return jsonify({"message":"i love you"})

if __name__ == "__main__":
    app.run(host = '0.0.0.0',port=5000)