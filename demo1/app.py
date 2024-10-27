from flask import Flask

app = Flask(__name__)

@app.route('/')

def functions():
    return "hello my dear thala"
if __name__ == "__main__":
    app.run(host= "0.0.0.0",port="7001")