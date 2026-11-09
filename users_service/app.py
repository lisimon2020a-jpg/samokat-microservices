from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "Иван", "phone": "+79991112233", "role": "customer"},
    {"id": 2, "name": "Анна", "phone": "+79994445566", "role": "courier"}
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(port=5001, debug=True)