from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

# Query parameters parser
query_parser = reqparse.RequestParser()
query_parser.add_argument('name', type=str, required=True, help='Name cannot be blank', location='args')
query_parser.add_argument('age', type=int, help='Age of the user', location='args')

# Form parameters parser
form_parser = reqparse.RequestParser()
form_parser.add_argument('name', type=str, required=True, help='Name cannot be blank', location='form')
form_parser.add_argument('email', type=str, required=True, help='Email cannot be blank', location='form')

# JSON parameters parser
json_parser = reqparse.RequestParser()
json_parser.add_argument('name', type=str, required=True, help='Name cannot be blank', location='json')
json_parser.add_argument('email', type=str, required=True, help='Email cannot be blank', location='json')


class UserResource(Resource):
    # Handle query parameters
    def get(self):
        args = query_parser.parse_args()
        name = args['name']
        age = args['age']
        return {'name': name, 'age': age}

    # Handle form parameters
    def post(self):
        args = form_parser.parse_args()
        name = args['name']
        email = args['email']
        return {'name': name, 'email': email}, 201

    # Handle JSON parameters
    def put(self):
        args = json_parser.parse_args()
        name = args['name']
        email = args['email']
        return {'name': name, 'email': email}, 200


api.add_resource(UserResource, '/user')

if __name__ == '__main__':
    app.run(debug=True)
