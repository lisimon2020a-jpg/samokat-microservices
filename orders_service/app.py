from flask import Flask, jsonify

app = Flask(__name__)

# История заказов (пустая по умолчанию)
orders = []

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

if __name__ == '__main__':
    app.run(port=5003, debug=True)