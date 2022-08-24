import random


# 1. 定义一个函数，函数可以返回参数的平方（n ** 2），请随机传入5个数字，并将它们返回的结果相加。
def func1(num):
    print(num)
    return num ** 2


# r = 0
# for i in range(5):
#     a = func1(random.randint(1, 10))
#     print(a)
#     r += a
# print(r)


# 2. 定义一个函数，接收3个字符串，要求返回3个字符串逆序连接后的数据。如输入123，123,123，最后返回321321321。
def func2(s1, s2, s3):
    print(s3[::-1] + s2[::-1] + s1[::-1])


# func2("123", "123", "123")

# 3. 定义一个函数，接收两个列表，将列表1中索引不能被2整除的数据和列表2中索引能被2整除的数据相拼接。
def func3(l1, l2):
    # 不是列表  重点是索引的取值  也就是每次循环i的值  0 1 2
    # 对索引进行判断， 当索引除以2能够除尽的时候  我们用索引去取列表2的值
    # 除以2不能除尽的时候  取列表1当中的数据
    # 仅限于两个列表的长度相同的情况
    s = ""
    for i in range(len(l1)):  # 0 1 2  l1
        if i % 2 != 0:
            s += str(l1[i])
        else:
            s += str(l2[i])
    print(s)


# func3([1, 2, 3], "456")

# 4. 定义一个函数，接收一个字符串和列表，判断字符串是否是列表中的数据，如果是，则删除，如果不是，就添加到列表中。
def func4(s, l):
    if s in l:
        l.remove(s)
    else:
        l.append(s)
    print(l)

    # 列表中存在多个字符串的时候
    # for i in range(l.count("abc")):
    #     l.remove(s)
    # print(l)


func4(input("字符串："), eval(input("列表:")))

# def func1(a,b):
#     if a not in b:
#         b.append(a)
#     else:
#      for i in range(len(b)):
#         if a in b :
#             b.remove(a)
#     print(b)
#
#
# func1(12, ['df','we2',12,23,3,4,'df4d'])


# 5. 定义一个函数，接收两个1到9之间的数字，根据传入的数字打印九九乘法表，如（3,5）， 就打印第3行到第5行的表达式。
def func5(num1, num2):
    if num1 < num2:
        for i in range(num1, num2 + 1):
            for j in range(1, i + 1):
                print(f"{j} * {i} = {j * i}", end="\t")
            print()
    else:
        for i in range(num2, num1+ 1):
            for j in range(1, i + 1):
                print(f"{j} * {i} = {j * i}", end="\t")
            print()


# func5(5, 2)
