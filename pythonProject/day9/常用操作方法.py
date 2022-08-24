# t1 = (0, 1, "2", 3, 4, "2", [1, 2, 3])

# 下标去查找数据
# print(t1[0])

# index  参考列表和字符串  返回数据在元组中的下标  如果没有找到  报错
# print(t1.index(2))

# count()  统计数据在元组中出现的次数
# print(t1.count("2"))

# len() 元组的长度  元组中数据的数量  length
# print(len(t1))
#
# t1[0] = "abc"
# print(t1)
# print(t1[-1])
# t1[-1][1] = "崔健"
# print(t1)

# for i in range(len(t1)):
#     print(t1[i])

# i = 0
# while i < len(t1):
#     print(t1[i])
#     i += 1

# 通过循环来获取序列中的数据
# 1. 直接通过for循环来遍历序列（字符串，列表，元组）
# 2. 通过for循环遍历当前序列的索引  range(len())
# 3. while循环遍历当前序列的索引  需要注意的是  小于 以及小于等于不同的判断

# 求 4 5 6 相加的结果
s = 0
t2 = (1, 2, 3, (4, 5, 6, "123"))
for i in t2:
    if isinstance(i, tuple):
        for j in i:
            if isinstance(j, str):
                s += eval(j)
            else:
                s += j
print(s)



