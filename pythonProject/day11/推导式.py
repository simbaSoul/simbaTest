# 列表推导式
# 创建一个列表 列表中添加0~9的数字
# while 写法
# l = []
# i = 0
# while i<10:
#     l.append(i)
#     i+=1
# print(l)
# l = [i for i in range(10)]


# 创建0-10的偶数列表
# b = []
# a = 0
# while a < 11:
#     if a % 2 == 0:
#         b.append(a)
#     a += 1
# print(b)
# l = [i for i in range(11) if i % 2 == 0]
# for i in range(11):
#     if i % 2 == 0:
#         l.append(i)
# print(l)
# l = [i for i in range(0, 11, 2)]
# print(l)

# [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
# l = []
# for i in range(1, 3):
#     for j in range(3):
#         if j % 2 == 0:
#             l.append((i, j))
# l = [(i, j) for i in range(1, 3) for j in range(3) if j % 2 == 0]
# print(l)
# list1 = ['name', 'age', 'gender']
# list2 = ['Tom', 20, 'man']
# zd = {}
# for i in range(len(list1)):
#     zd[list1[i]] = list2[i]
# print(zd)

# 创建一个字典：字典key是1-5数字，value是这个数字的2次方。
# d = {i: i ** 2 for i in range(1, 6)}
# # for i in range(1, 6):
# #     d[i] = i ** 2
# print(d)

# 提取value值大于200的数据
counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}

d = {k: v for k,v in counts.items() if v >= 200}
# for k,v in counts.items():
#     if v >= 200:
#         d[k] = v
# print(d)


# 创建一个集合，数据为下方列表的2次方。
list1 = [1, 1, 2]
s = {i ** 2 for i in list1}
# for i in list1:
#     s.add(i ** 2)
print(s)

