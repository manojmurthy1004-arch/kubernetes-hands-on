from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Jenkins Multi-Stage Pipeline! Engineered by MANOJ MURTHY S (1BM24IS411)"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
