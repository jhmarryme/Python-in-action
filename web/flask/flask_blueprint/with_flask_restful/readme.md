
使用 Blueprint 和 flask_restful 构建模块化的 RESTful API。

示例包括两个模块：auth 模块和 products 模块。

## 测试 API

1. **启动应用程序**
    
    ```bash
    python app.py
    
    ```
    
2. **测试 `auth` 模块**
    - **登录**：
        
        ```bash
        curl -X POST -H "Content-Type: application/json" -d '{"username": "admin", "password": "password"}' http://127.0.0.1:5000/auth/login
        
        ```
        
    - **登出**：
        
        ```bash
        curl -X POST http://127.0.0.1:5000/auth/logout
        
        ```
        
3. **测试 `products` 模块**
    - **获取产品列表**：
        
        ```bash
        curl http://127.0.0.1:5000/products/
        
        ```
        
    - **添加新产品**：
        
        ```bash
        curl -X POST -H "Content-Type: application/json" -d '{"name": "Tablet", "price": 299.99}' http://127.0.0.1:5000/products/
        
        ```
        
    - **获取单个产品**：
        
        ```bash
        curl http://127.0.0.1:5000/products/1
        
        ```
        
    - **删除产品**：
        
        ```bash
        curl -X DELETE http://127.0.0.1:5000/products/1
        
        ```