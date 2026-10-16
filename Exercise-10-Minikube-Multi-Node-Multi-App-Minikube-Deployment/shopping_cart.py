from flask import Flask, jsonify, request

app = Flask(__name__)

cart = []

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "service": "Shopping Cart Service",
        "student": "MANOJ MURTHY S (1BM24IS411)",
        "status": "online"
    })

@app.route("/cart", methods=["GET"])
def get_cart():
    return jsonify(cart)

@app.route("/cart", methods=["POST"])
def add_to_cart():
    item = request.json or {}
    cart.append(item)
    return jsonify(cart), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
