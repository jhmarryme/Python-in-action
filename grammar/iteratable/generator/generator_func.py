def my_generator():
    my_num = 0
    while my_num < 5:
        yield my_num
        my_num += 1


# 得到一个生成器对象
generator_ = my_generator()
print(type(generator_))
