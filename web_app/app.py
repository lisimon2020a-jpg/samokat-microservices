from flask import Flask, render_template, request, redirect, url_for, flash
import httpx

app = Flask(__name__)
app.secret_key = 'samokat-secret-key'

API_GATEWAY_URL = "http://localhost:8000"
TIMEOUT = 5.0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    try:
        response = httpx.get(f"{API_GATEWAY_URL}/products", timeout=TIMEOUT)
        response.raise_for_status()
        return render_template('products.html', products=response.json())
    except httpx.HTTPError as e:
        flash(f"Ошибка загрузки товаров: {str(e)}", "error")
        return render_template('products.html', products=[])

@app.route('/orders', methods=['GET', 'POST'])
def orders():
    if request.method == 'POST':
        try:
            order_data = {
                "product_id": int(request.form['product_id']),
                "user_id": int(request.form['user_id']),
                "quantity": int(request.form['quantity'])
            }
            response = httpx.post(f"{API_GATEWAY_URL}/orders", json=order_data, timeout=TIMEOUT)
            response.raise_for_status()
            flash("Заказ успешно создан!", "success")
            return redirect(url_for('orders'))
        except (httpx.HTTPError, ValueError) as e:
            flash(f"Ошибка создания заказа: {str(e)}", "error")

    try:
        response = httpx.get(f"{API_GATEWAY_URL}/orders", timeout=TIMEOUT)
        response.raise_for_status()
        return render_template('orders.html', orders=response.json())
    except httpx.HTTPError as e:
        flash(f"Ошибка загрузки заказов: {str(e)}", "error")
        return render_template('orders.html', orders=[])

@app.route('/users')
def users():
    try:
        response = httpx.get(f"{API_GATEWAY_URL}/users", timeout=TIMEOUT)
        response.raise_for_status()
        return render_template('users.html', users=response.json())
    except httpx.HTTPError as e:
        flash(f"Ошибка загрузки пользователей: {str(e)}", "error")
        return render_template('users.html', users=[])

if __name__ == '__main__':
    app.run(port=5004, debug=True)