from flask import Flask, jsonify, render_template, request
from main import cart 
from main import transaction as trans
from main import rabbitmq as rabbit
from main import stock
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transaction')
def transaction():
    return render_template('transaction.html', transaction= trans.get())

@app.route('/cart')
def panier():
    return render_template('cart.html', panier = cart.get())


@app.route('/cart/acheter')
def acheter_panier():
    cart.send()
    return render_template('transaction.html', transaction= trans.get())


@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    print("Nous sommes ici : app")
    data = request.json
    print(data)
    product_name = data['product']
    price = int(data['price'])
    quantity = int(data['quantity'])
    message = cart.add_to_cart(product_name,price,  quantity)
    return jsonify({'message': message})



@app.route('/rabbitmq')
def rabbitmq():
    return rabbit.get()
   



@app.route('/products')
def products():
    return render_template('products.html', products = stock.get())

if __name__ == '__main__':
    app.run(debug=True)
