from flask import Blueprint
from flask_restful import Api

from .resources import ProductListResource, ProductResource

# 创建 Blueprint
products_bp = Blueprint('products', __name__, url_prefix='/products')

# 创建 Api 对象并注册资源
products_api = Api(products_bp)
products_api.add_resource(ProductListResource, '/')
products_api.add_resource(ProductResource, '/<int:product_id>')
