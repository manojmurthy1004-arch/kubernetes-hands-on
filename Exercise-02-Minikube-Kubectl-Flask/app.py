from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask on Kubernetes! Deployed by MANOJ MURTHY S (USN: 1BM24IS411)"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=15000)
