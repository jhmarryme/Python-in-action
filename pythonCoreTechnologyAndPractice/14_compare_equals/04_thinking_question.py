import copy

if __name__ == '__main__':
    x = [1]
    x.append(x)
    y = copy.deepcopy(x)
    # 以下命令的输出是？
    print(x == y)
