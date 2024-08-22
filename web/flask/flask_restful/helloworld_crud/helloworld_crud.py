import sqlite3

from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


def get_db():
    conn = sqlite3.connect('user.db')
    return conn


# 创建用户表
def init_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS users')
    cursor.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


init_db()


# RESTful 资源类
class UserResource(Resource):
    # 查询用户（通过路径参数或查询参数）
    def get(self, user_id=None):
        conn = get_db()
        cursor = conn.cursor()
        if user_id:
            cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
            user = cursor.fetchone()
            conn.close()
            if user:
                return jsonify({'id': user[0], 'name': user[1], 'email': user[2]})
            return {'message': 'User not found'}, 404
        else:
            name = request.args.get('name')
            if name:
                cursor.execute('SELECT * FROM users WHERE name = ?', (name,))
                user = cursor.fetchone()
                conn.close()
                if user:
                    return jsonify({'id': user[0], 'name': user[1], 'email': user[2]})
                return {'message': 'User not found'}, 404
            conn.close()
            return {'message': 'No user ID or name provided'}, 400

    # 创建新用户（表单参数）
    def post(self):
        name = request.form['name']
        email = request.form['email']
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
        conn.commit()
        user_id = cursor.lastrowid
        conn.close()
        return {'message': 'User created', 'user_id': user_id}, 201

    # 更新用户信息（路径参数和 JSON 参数）
    def put(self, user_id):
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        conn = get_db()
        cursor = conn.cursor()
        if name:
            cursor.execute('UPDATE users SET name = ? WHERE id = ?', (name, user_id))
        if email:
            cursor.execute('UPDATE users SET email = ? WHERE id = ?', (email, user_id))
        conn.commit()
        conn.close()
        return {'message': 'User updated'}, 200

    # 删除用户（路径参数）
    def delete(self, user_id):
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
        conn.commit()
        conn.close()
        return {'message': 'User deleted'}, 200


# 设置路由
api.add_resource(UserResource, '/user', '/user/<int:user_id>')

if __name__ == '__main__':
    app.run(debug=True)
