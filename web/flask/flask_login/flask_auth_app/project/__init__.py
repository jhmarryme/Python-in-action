import os

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# 初始化 SQLAlchemy 数据库实例
db = SQLAlchemy()


def create_app():
    """
    创建并配置 Flask 应用实例的工厂函数
    """
    app = Flask(__name__)  # 创建 Flask 应用实例
    app.config['SECRET_KEY'] = 'secret-key-goes-here'  # 配置应用的密钥，用于会话和加密
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'data.sqlite')  # 配置数据库 URI
    db.init_app(app)  # 初始化数据库连接

    # 初始化 Flask-Login 管理器
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'  # 设置登录视图的端点，当未登录时会重定向到该视图
    login_manager.init_app(app)  # 将登录管理器绑定到应用

    # 导入用户模型，用于加载用户
    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        """
        使用用户 ID 从数据库中加载用户
        :param user_id: 用户的主键 ID
        :return: 用户对象或 None
        """
        return User.query.get(int(user_id))  # 根据主键 ID 查询用户

    # 注册认证相关的蓝图
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # 注册非认证相关的蓝图
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app  # 返回配置完成的应用实例
