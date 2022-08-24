# 需求：有变量a = 10 和b = 20 ，交换两个变量的值。
a = 10
b = 20

# 借助一个第三方变量
# c = a   # c = a = 10
# a = b   # a = 20
# b = c
# print(a, b)

a, b = b, a
print(a, b)

