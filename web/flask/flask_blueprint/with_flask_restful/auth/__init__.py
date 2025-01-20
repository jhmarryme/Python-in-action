from flask import Blueprint
from flask_restful import Api

from .resources import LoginResource, LogoutResource

# 创建 Blueprint
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# 创建 Api 对象并注册资源
auth_api = Api(auth_bp)
auth_api.add_resource(LoginResource, '/login')
auth_api.add_resource(LogoutResource, '/logout')
