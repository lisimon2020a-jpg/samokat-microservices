from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {"id": 101, "name": "Круассан", "price": 149.0, "stock": 10},
    {"id": 102, "name": "Йогурт", "price": 89.0, "stock": 25}
]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

if __name__ == '__main__':
    app.run(port=5002, debug=True)