import flask

app = flask.Flask(__name__)  # Use Flask class correctly
@app.route('/')
def test():
    return "hello world"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Corrected 'hots' to 'host'
