from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from . import db  # 导入数据库实例
from .models import User  # 导入用户模型

# 创建一个名为 auth 的 Blueprint，用于管理认证相关的路由
auth = Blueprint('auth', __name__)


# 显示登录页面的路由
@auth.route('/login')
def login():
    return render_template('login.html')  # 渲染登录页面模板


# 处理登录表单提交的路由
@auth.route('/login', methods=['POST'])
def login_post():
    # 从表单中获取用户提交的数据
    email = request.form.get('email')  # 获取用户输入的邮箱
    password = request.form.get('password')  # 获取用户输入的密码
    remember = True if request.form.get('remember') else False  # 检查是否选中“记住我”选项

    # 根据邮箱从数据库中查询用户
    user = User.query.filter_by(email=email).first()

    # 验证用户是否存在以及密码是否正确
    if not user or not check_password_hash(user.password, password):
        # 如果用户不存在或密码错误，显示错误消息并重新加载登录页面
        flash('请检查您的登录信息并重试。')
        return redirect(url_for('auth.login'))

    # 如果验证通过，登录用户并根据“记住我”选项设置会话
    login_user(user, remember=remember)

    # 登录成功后重定向到用户的个人主页
    return redirect(url_for('main.profile'))


# 显示注册页面的路由
@auth.route('/signup')
def signup():
    return render_template('signup.html')  # 渲染注册页面模板


# 处理注册表单提交的路由
@auth.route('/signup', methods=['POST'])
def signup_post():
    # 从表单中获取用户提交的数据
    email = request.form.get('email')  # 获取用户输入的邮箱
    name = request.form.get('name')  # 获取用户输入的姓名
    password = request.form.get('password')  # 获取用户输入的密码

    # 检查数据库中是否已存在相同邮箱的用户
    user = User.query.filter_by(email=email).first()

    if user:
        # 如果邮箱已存在，显示错误消息并重定向回注册页面
        flash('该邮箱地址已被注册')
        return redirect(url_for('auth.signup'))

    # 创建新用户，并使用哈希算法对密码进行加密存储
    new_user = User(email=email, name=name, password=generate_password_hash(password))

    # 将新用户添加到数据库并提交更改
    db.session.add(new_user)
    db.session.commit()

    # 注册成功后重定向到登录页面
    return redirect(url_for('auth.login'))


# 处理用户注销的路由
@auth.route('/logout')
@login_required  # 确保用户已登录后才能注销
def logout():
    logout_user()  # 注销当前用户
    return '注销成功'  # 返回注销成功的消息
