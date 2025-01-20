from flask_restful import Resource, reqparse

# 假设一个简单的内存数据存储
products = [
    {'id': 1, 'name': 'Laptop', 'price': 999.99},
    {'id': 2, 'name': 'Smartphone', 'price': 499.99}
]

# 产品列表资源
class ProductListResource(Resource):
    def get(self):
        return {'products': products}, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True, help='Product name is required')
        parser.add_argument('price', type=float, required=True, help='Product price is required')
        args = parser.parse_args()

        new_product = {
            'id': len(products) + 1,
            'name': args['name'],
            'price': args['price']
        }
        products.append(new_product)
        return new_product, 201

# 单个产品资源
class ProductResource(Resource):
    def get(self, product_id):
        product = next((p for p in products if p['id'] == product_id), None)
        if product:
            return product, 200
        return {'message': 'Product not found'}, 404

    def delete(self, product_id):
        global products
        products = [p for p in products if p['id'] != product_id]
        return {'message': 'Product deleted'}, 200
