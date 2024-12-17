'''
期望输出结果:
[{'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'},
{'name': 'mike', 'dob': '1999-01-01', 'gender': 'male'},
{'name': 'nancy', 'dob': '2001-02-01', 'gender': 'female'}]
'''
if __name__ == '__main__':
    attributes = ['name', 'dob', 'gender']
    values = [
        ['jason', '2000-01-01', 'male'],
        ['mike', '1999-01-01', 'male'],
        ['nancy', '2001-02-01', 'female']
    ]
    result = []

    # 多行条件循环语句 实现
    for value in values:
        tmp = {}
        for index in range(0, len(attributes)):
            tmp[attributes[index]] = value[index]
        result.append(tmp)
    print(result)
    # 一行条件循环语句 实现
    result = [dict(zip(attributes, value)) for value in values]
    print(result)
