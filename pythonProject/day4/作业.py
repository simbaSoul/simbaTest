# 1. 定义一个函数，接收一个1~100之间的数字，对数字进行判断，60以下不及格，60~90之间为良好，90以上为优秀，超出范围提示输入有误。
def fun1(num):
    if 0 <= num < 60:
        print("不及格")
    elif 60 <= num < 90:
    # elif (num >= 60) and (num <= 90)
        print("良好")
    elif 90 <= num <= 100:
        print("优秀")
    else:
        print("输入有误")


# fun1(int(input("请输入您的成绩:")))

# 2. 根据公式：孩子身高 = （父亲身高+母亲身高）* 0.54，请用户输入父母身高，单位是米，计算孩子的身高，保留两位小数
def fun2(f, m):
    return (f + m) * 0.54


# print("孩子的身高是%.2f米" % fun2(1.80, 1.70))

# 3. 随机生成两个数字，然后输入一个指定的运算符，让两个数字执行对应的运算
# 导入随机数模块
import random


def fun3(num1, num2, s):
    """
    :param num1: 随机数1
    :param num2: 随机数2
    :param s: 运算符
    :return:
    """
    # 根据接收到的运算符，对两个数字进行相应的计算  +  num1+num2  - num1-num2
    if s == "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif s == "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    elif s == "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    elif s == "/":
        print(f"{num1} / {num2} = {num1 / num2}")
    elif s == "//":
        print(f"{num1} // {num2} = {num1 // num2}")
    elif s == "%":
        print(f"{num1} % {num2} = {num1 % num2}")


# fun3(random.randint(1, 100), random.randint(1, 100), input("请输入您的运算符:"))


# 4. 定义一个函数，接收任意两个数字，如果数字1大于数字2，就返回数字1的平方，否则返回数字2的平方，使用三目运算符实现
def func4(num1, num2):
    return num1 ** 2 if num1 > num2 else num2 ** 2


print(f"结果是{func4(10, 20)}")
