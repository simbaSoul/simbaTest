# int() 将括号内的数据转换为int 数据类型
# 数据一定得是字符串形式的整数
# a = input("请输入您的数字:")
# print(type(int(a)))

# float  将整型或字符串类型的数字转换为浮点型
# a = 10
# b = "10.1"
# print(float(a))
# print(type(float(a)))
# print(float(b))
# print(type(float(b)))

# str()  将数据转换为字符串类型
# num = 1
# print(str(num))
# print(type(str(num)))
# num2 = 1.0
# print(str(num2))
# print(type(str(num2)))


# eval 还原字符串的数据类型  “1”
# num1 = "1"
# print(type(eval(num1)))
# num2 = "1.0"
# print(type(eval(num2)))
# list1 = "[1, 2, 3]"
# print(type(eval(list1)))

# tuple() 将序列（列表）转换为元组
# list1 = [1, 2, 3]
# mytuple = tuple(list1)
# print(type(tuple(list1)))

# list() 将序列转换为列表
# tuple1 = (1, 2, 3)
# print(type(tuple1))
# print(type(list(tuple1)))

# set()  将序列转换为集合  天然去重
list1 = [1, 1, 2, 2]
print(list1)
myset = set(list1)
print(myset)
