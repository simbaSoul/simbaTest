# a = 1, 2, 3, 4, 5
# print(a)
# print(type(a))

# def func():
#     return 1, 2, 3
#
#
# a = func()


# a, b, c = (1, 2, 3)
# print(a,b,c)

# 字典的拆包 是把键赋值给对应的变量
dict1 = {'name': 'TOM', 'age': 18}
a, b = dict1

print(a)
print(b)

print(dict1[a])
print(dict1.get(b))
