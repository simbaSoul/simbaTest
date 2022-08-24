# 1. 有列表students = [{'name': 'TOM', 'age': 20},{'name': 'ROSE', 'age': 19},{'name': 'Jack', 'age': 22}]，
# 请根据年龄大小对字典排序
def fun1(l):
    # age_l = []
    # for i in l:
    #     age_l.append(i['age'])
    # age_l.sort()
    # print(age_l)
    # new_l = []
    # for i in age_l:  # 19  20
    #     for j in l:
    #         if i == j['age']:
    #             new_l.append(j)
    #             break
    # print(new_l)

    al = [i['age'] for i in l]
    al.sort()
    nl = [j for i in al for j in l if i == j['age']]
    print(nl)


# fun1([{'name': 'TOM', 'age': 20},{'name': 'ROSE', 'age': 19},{'name': 'Jack', 'age': 22}])

# 2. 定义函数，求数字6的阶乘（6*5*4*3*2*1）
def func2(num):
    if num == 1:
        return 1
    return num * func2(num - 1)


# print(func2(6))

# 3. 使用 lambda 对元组列表[(‘English’， 88)， （‘Science’， 90）， （‘Maths’， 97）， （‘Social sciences’， 82）]根据数字进行排序。
def func3(l):
    l.sort(key=lambda i: i[1])
    print(l)


# func3([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])

# 4. 使用 lambda 对字典列表 [{'name': 'ls', 'age': 27}, {'name': 'zs', 'age': 21}, {'name': 'ww', 'age': 23}] 根据age进行排序
def func4(l):
    # sort 用于排序 当sort排序的数据是序列的时候  通过key来指定排序的标准 根据什么样的数据来排序
    l.sort(key=lambda x: x['name'])
    print(l)


# func4([{'name': 'ls', 'age': 27}, {'name': 'zs', 'age': 21}, {'name': 'ww', 'age': 23}])


# 5. 使用 lambda 判断字符串是否以给定字符开头
def func5():
    flag = lambda x: x.startswith("a")
    print(flag("bc"))


func = lambda str,zc: True if str.find(zc) == 0 else False

# func5()

# 6. 使用 lambda 对[1, 2, 3, 5, 7, 8, 9, 10]中奇偶数进行计数
def func6(l):
    l1_len = len(list(filter(lambda i: i % 2 == 0, l)))
    l2_len = len(list(filter(lambda i: i % 2 != 0, l)))
    print(f"偶数有{l1_len}个")
    print(f"奇数有{l2_len}个")


# func6([1, 2, 3, 5, 7, 8, 9, 10])

# 7. 使用 map 和 lambda 对[1, 2, 3],[4, 5, 6]两个列表中的数据相加，最后结果应为[5, 7, 9]
def func7(a, b):
    result = map(lambda i, j: i+j, a, b)
    print(list(result))


func7([1, 2, 3], [4, 5, 6])
