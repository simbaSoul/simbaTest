# # abs 求绝对值
# print(abs(-10))
# # round  四舍五入
# print(round(1.1))
# print(round(1.5))

# 任意两个数字，先得到他们的绝对值再进行求和计算。
# def fun1(a, b):
#     return abs(a) + abs(b)

#
# fun1 = lambda a, b: abs(a) + abs(b)
# print(fun1(-3, -2))


def fun1(a, b, c):
    return c(a) + c(b)  # c = abs   abs(a) + abs(b)


fun1(1.1, 2.5, round)