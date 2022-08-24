# 1. 请编写函数，实现列表的快速去重
import random


def func1(l):
    l1 = []
    # for i in l:
    #     if i not in l1:
    #         l1.append(i)
    # print(l1)
    d = {}
    for i in l:
        d[i] = 0
    for key in d.keys():
        l1.append(key)
    print(l1)


# func1([1, 1, 2, 2])


def fum1(a):
    for i in a:
        if a.count(i)>1:
            print(a.count(i))
            a.remove(i)
    print(a)


# fum1(['qw','qw','qw','qw','12','21'])

# 2. 定义一个函数，接受一个列表和一个元组，将他们包含的数据连接后打印。
def func2(l, t):
    l.extend(t)
    # print(l)
    s = ""
    for i in l:
        s += str(i)  # s = "1" + "2"  + "3"  + ""
    # print(s)
    # print("".join(l))


# func2([1, 2, 3], (4, 5, 6))

# 3. 现有列表['python', 'java', 'html', 'C', 'C++', 'JS']，将其中长度大于等于3的数据添加到元组中，并且首字母全部大写
def func3(l):
    l1 = []
    for i in l:
        if len(i) >= 3:
            l1.append(i.title())
    print(tuple(l1))


# func3(['python', 'java', 'html', 'C', 'C++', 'JS'])


# 4. 有列表1[1, 3, 5]，列表2[3, 4]，将列表1的数据依次和列表2的数据进行比较，如果数据不同，则将两个数据打包成元组，
# 并将元组添加到一个列表中，即最后的结果是[(1,3), (1,4), (3,4), (5, 3), (5, 4)]
def func4(l1, l2):
    l = []
    for i in l1:
        for j in l2:
            if i != j:
                l.append((i, j))
    print(l)


# func4([1, 3, 5], [3, 4])

# 5. 请随机生成20个1~10之间的数字添加到列表当中，并统计每个数字出现的次数，要求最终展示结果为字典，如{'10': 2, '4':3}
def func5():
    l = []
    for i in range(20):
        l.append(random.randint(1, 10))
    print(l)
    d = {}
    for i in set(l):  # i = 3
        d[i] = l.count(i)
    print(d)


# func5()

# 6. 有字典{'num1': 20, 'num2': 10, 'num3':30}，请获取所有的值并排序输出。
# d = {'num1': 20, 'num2': 10, 'num3':30}
# l = []
# for value in d.values():
#     l.append(value)
# l.sort()
# print(l)
