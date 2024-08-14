# 思考题
# 1 将字典按值从大到小排序
import operator

if __name__ == '__main__':
    d = {"mike": 10, "lucy": 2, "ben": 30}
    print(d.items())
    sort_d = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
    print(sort_d)
