学习记录:

https://www.notion.so/17e0c1dc367680e58dcdd71822b36d08


测试命令:

```shell

# 创建用户
curl -X POST http://127.0.0.1:5000/user -H "Content-Type: application/json" -d '{"username": "john", "email": "john@example.com"}'

# 获取所有用户
curl http://127.0.0.1:5000/users

# 更新用户
curl -X PUT http://127.0.0.1:5000/user/1 -H "Content-Type: application/json" -d '{"username": "john_doe"}'

# 删除用户
curl -X DELETE http://127.0.0.1:5000/user/1

```