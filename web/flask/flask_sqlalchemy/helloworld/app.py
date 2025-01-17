import os

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# 创建 Flask 应用实例
app = Flask(__name__)

# 配置数据库 URI 和关闭修改监控以提升性能
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化 SQLAlchemy 数据库对象
db = SQLAlchemy(app)


# 定义用户模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 主键 ID
    username = db.Column(db.String(80), unique=True, nullable=False)  # 用户名，唯一且必填
    email = db.Column(db.String(120), unique=True, nullable=False)  # 邮箱，唯一且必填

    def __repr__(self):
        return f'<User {self.username}>'  # 用户对象的字符串表示


# 创建用户的路由（POST 请求）
@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()  # 从请求体中解析 JSON 数据
    new_user = User(username=data['username'], email=data['email'])  # 创建新的用户对象
    db.session.add(new_user)  # 添加用户到数据库会话
    db.session.commit()  # 提交更改到数据库
    return jsonify({'message': '用户创建成功'}), 201  # 返回成功响应


# 获取所有用户的路由（GET 请求）
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()  # 查询所有用户数据
    # 将用户数据序列化为字典列表并返回 JSON 格式
    return jsonify([{'id': user.id, 'username': user.username, 'email': user.email} for user in users])


# 更新指定用户的路由（PUT 请求）
@app.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()  # 从请求体中解析 JSON 数据
    user = User.query.get(id)  # 根据 ID 查询用户
    if not user:
        return jsonify({'message': '用户未找到'}), 404  # 如果用户不存在，返回 404 错误
    # 更新用户属性，如果没有提供新值则保持原值
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    db.session.commit()  # 提交更改到数据库
    return jsonify({'message': '用户更新成功'})  # 返回成功响应


# 删除指定用户的路由（DELETE 请求）
@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)  # 根据 ID 查询用户
    if not user:
        return jsonify({'message': '用户未找到'}), 404  # 如果用户不存在，返回 404 错误
    db.session.delete(user)  # 从数据库中删除用户
    db.session.commit()  # 提交更改到数据库
    return jsonify({'message': '用户删除成功'})  # 返回成功响应


# 如果此文件被直接运行，则启动 Flask 应用
if __name__ == '__main__':
    app.run(debug=True)  # 启用调试模式，便于开发
