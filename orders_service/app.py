from flask import Flask, jsonify, request

app = Flask(__name__)

orders = []

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

@app.route('/orders', methods=['POST'])
def create_order():
    # Получаем JSON из запроса
    order_data = request.json
    # Добавляем ID заказу
    order_data['id'] = len(orders) + 1
    orders.append(order_data)
    return jsonify(order_data), 201

if __name__ == '__main__':
    app.run(port=5003, debug=True)