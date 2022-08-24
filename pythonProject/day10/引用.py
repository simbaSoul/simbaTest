# a = 1
# b = a

# print(b)
# print(id(a))
# print(id(b))

# a = 2
# print(b)

# print(id(a))
# print(id(b))


# l = [1, 2, 3, 4]
# print(id(l))
# l[0] = 100
# print(id(l))

def test1(a):
    print(a)
    print(id(a))
    a += a
    print(a)
    print(id(a))
    print('---------------')


# int：计算前后id值不同
# b = 100
# test1(b)
# 列表：计算前后id值相同
# c = [11, 22]
# test1(c)


