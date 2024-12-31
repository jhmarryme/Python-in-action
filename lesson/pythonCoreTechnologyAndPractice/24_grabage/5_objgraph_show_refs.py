import objgraph

# 创建两个列表
a = [1, 2, 3]
b = [4, 5, 6]

# 创建循环引用：a 引用 b，b 引用 a
a.append(b)
b.append(a)

# 生成引用关系图
objgraph.show_refs([a])