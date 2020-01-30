from flask  import Flask, jsonify

app = Flask (__name__)

from products import products



@app.route('/prueba')
def productos():
    return jsonify({"menssaje": "Es una puta prueba" })

@app.route('/products')
def getProducts():
    return jsonify(products) 


@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        return jsonify({"Product": productsFound[0]})
    return jsonify({"message": "Product not found"})

@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(new_product)
    return jsonify({"message": "Product Added Succesfully", "products": products})

@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound) > 0):
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantitsy'] = request.json['quantity']
        return jsonify({
            "message": "Product Update",
            "product": productFound[0]
        })
    return jsonify({"message": "Product Not Found"})    

@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if len(productsFound) > 0:
        products.remove(productsFound[0])
        return jsonify({
            "message": "Product Deleted",
            "products": products
        })
        return jsonify({"message": "Product Not Found"})

if __name__ == '__main__':
    app.run(debug=True, port=4000)