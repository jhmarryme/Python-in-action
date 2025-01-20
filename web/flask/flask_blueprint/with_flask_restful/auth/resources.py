from flask_restful import Resource, reqparse


# 登录资源
class LoginResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True, help='Username is required')
        parser.add_argument('password', required=True, help='Password is required')
        args = parser.parse_args()

        # 模拟验证
        if args['username'] == 'admin' and args['password'] == 'password':
            return {'message': 'Login successful'}, 200
        return {'message': 'Invalid credentials'}, 401


# 登出资源
class LogoutResource(Resource):
    def post(self):
        return {'message': 'Logged out successfully'}, 200
