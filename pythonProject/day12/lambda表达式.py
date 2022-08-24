# def func1():
#     return 200
#
#
# print(func1)
# print(func1())
#
# # lambda表达式
#
# func2 = lambda: 200
# print(func2)
# print(func2())

# def add_sum(num1, num2):
#     return num1 + num2
#
#
# result = add_sum(10, 20)
# print(result)

# add1 = lambda num1, num2: num1 + num2
# result2 = add1(10, 20)
# print(result2)


# def dir1(**kwargs):
#     return kwargs
#
#
# test1 = lambda **kwargs: kwargs
# print(test1(name="lhd", age=28))


# result = dir1(name="lhd", age=28)
# print(result)


# test1 = lambda *args: args
# print(dir1(1, 2, 3, 4))


# def func1(a, b):
#     return a if a > b else b


# func1 = lambda a, b: a if a > b else b
# print(func1(10, 9))

# 列表数据按字典key的值排序
students = [
    {'name': 'TOM', 'age': 20},
    {'name': 'ROSE', 'age': 19},
    {'name': 'Jack', 'age': 22}
]

# 按name值升序排列
# 排序是按照自然排序的规则来进行的  对列表中的数据进行遍历  【1,2,3,4】 【{}】 指定要根据哪个数据排序
# students.sort(key=lambda x: x['name'])
# print(students)


# 按name值降序排列
# students.sort(key=lambda x: x['name'], reverse=True)
# print(students)

#
# # 按age值升序排列   用于指定列表排序的依据  key  关键字
students.sort(key=lambda i: i['age'])
# print(students)




