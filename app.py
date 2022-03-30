from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>push to docker by using CircleCI</h2>'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)