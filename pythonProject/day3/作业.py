# 1. 通过Python代码实现：输入你的姓名，身高，体重，然后打印刚才输入的内容
# name = input("请输入您的姓名:")
# height = int(input("请输入您的身高:"))
# weight = float(input("请输入您的体重:"))
# print(f"姓名为{name}，身高为{height}米，体重为{weight}公斤")


# 2. 通过Python代码实现：输入两个数字，进行运算，并打印结果
# input 接收到的都是字符串  而字符串与字符串之间的 + 号 实现的是拼接的操作
# num1 = eval(input("请输入第一个数字："))
# num2 = eval(input("请输入第二个数字："))
# print(num1 + num2)

# 3. 定义一个函数，接收两个数字，并将它们相乘的结果返回，最后打印该结果的3次方。
# 指数 n次方   2 ** 3  2*2*2
# def test3(a, b):
#     return a * b
#
#
# print(test3(2, 3) ** 3)

# 4. 定义一个函数，接收一个数字，判断它是否能够被7整除，如果能就打印该数字，不能则给出相应提示
# 能被数字整除  指的是  除以这个数字能除尽  也就是没有余数
# def test4(num):
#     if num % 7 == 0:
#         print(f"{num}能够被7整除")
#     else:
#         print(f"{num}不能够被7整除")
#
#
# test4(eval(input("输个数字吧：")))


# 5. 定义一个函数，接收两个数字，要求返回他们的差，最后打印相同数量的*号
def test5(num1, num2):
    return num1 - num2


# num =   # num = 5
# print("*" * num)
print("*" * test5(10, 8))


# num = int(input('请输入您的数字：'))
# if num % 7 == 0 and 7 != 0:
#   print('符合')
# else:
#   print('不符合')


