import functools
import keyword


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def func1(x):
    return x % 2 == 0


result = filter(func1, list1)
print(list(result))


# 需求：计算list1 序列中各个数字的累加和。


# def func(a, b):
#     return a + b


# result = functools.reduce(func, range(1, 101))
# print(result)




# 需求：计算list1 序列中各个数字的2次方。
# def func(a):
#     return a ** 2
#
#
# result = map(func, list1)
# for i in result:
#     print(i)




