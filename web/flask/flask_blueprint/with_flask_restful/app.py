from flask import Flask

from auth import auth_bp
from products import products_bp

app = Flask(__name__)

# 注册 Blueprint
app.register_blueprint(auth_bp)
app.register_blueprint(products_bp)

if __name__ == '__main__':
    app.run(debug=True)
