from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is a secure Flask application running inside a Docker container! Configured by MANOJ MURTHY S (1BM24IS411)"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
