# len()  统计序列的长度  序列中的数据的数量
# print(len([1, 2, 3]))
# del  del()
# a = 10
# del a
# print(a)
# max()  求最大值
# print(max([1, 2, 3]))
# min()  求最小值
# print(min([1, 2, 3]))

# range() 生成一个数字区间  3个参数
# range(10)  0~9
# range(1, 10)  1 ~ 9
# for i in range(1, 10, 2):
#     print(i)
# for i in range(10, 1, -1):
#     print(i)

# enumerate  生成一个包含了索引和对应数据的集合
# l = [1, 2, 3]
# for i in enumerate(l):
#     print(i)
# for index,data in enumerate(l):
#     print(index, data)

# d = {'name': 'zs', 'age': 30}
# for i in d.items():
#     print(i)
# a = 1, 2
# print(a)
# a, b = 1, 2
# print(a, b)

# print(tuple([1, 2, 3]))
# print(tuple({1, 2, 3}))

# t = (1, 2, 3)
# tl = list(t)
# tl.remove(1)
# t1 = tuple(tl)
# print(t1)
# print(t)
# print(list((1, 2, 3)))
# print(list({1, 2, 3}))

# set()
l = [1, 2, 2]
# print(list(set(l)))
sl = str(l)  # [1, 2, 2]
l1 = eval(sl)
print(l1)
print(type(l1))





