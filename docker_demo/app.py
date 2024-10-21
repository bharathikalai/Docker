from flask import Flask requests

app = Flask(__name__)

@app.route('/')

def ajithkumar():
    return "thala pola varuma"
if __name__ == "__main__":
    app.run(host= "0.0.0.0",port="7777")