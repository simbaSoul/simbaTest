# 1. 使用for循环打印九九乘法表
# 列数/表达式的数量 * 行数 = 结果
# while循环
# i = 1
# while i <= 9:
#     j = 1
#     # 表达式的数量小于等于行数
#     while j <= i:
#         print(f"{j} * {i} = {j * i}", end="\t")
#         j += 1
#     print()
#     i += 1

# range(a, b) 函数 生成一个数字区间的序列  接收两个数字参数  a参数表示取值的最小范围  b参数表示取值的最大范围 但是不包含b本身
# for i in range(1, 5):
#     print(i)

# for循环
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(f"{j} * {i} = {j * i}", end="\t")
#     print()

# for i in  range(1,10):
#     for j in range(1, 10):
#         if i >= j:
#             print(f"{i}*{j}={i*j}",end="\t")
#         else:
#             break
#     print()

# 2. 求1~100之间能被3整除的数的和
# while循环写法
# i = 1
# r = 0
# while i <= 100:
#     if i % 3 == 0:
#         print(i)
#         r += i
#     i += 1
# print(r)

# for循环
# r = 0
# for i in range(1, 101):
#     if i % 3 == 0:
#         r += i
# print(r)

# 3. 打印1~100之间所有能被7整除以及包含7的数字  两位数的情况  个位是7  或者  十位是7
# for i in range(1, 101):
#     if i % 7 == 0 or i % 10 == 7 or i // 10 == 7:
#         print(i)

# 4. 求水仙花数，水仙花数指的是一个三位数，个位数的立方加十位数的立方加百位数的立方等于原数，如153，求所有的水仙花数。
# for i in range(100, 1000):
#     # 个位数  i % 10
#     # 十位数  i // 10 % 10
#     # 百位数  i // 100
#     if (i % 10) ** 3 + (i // 10 % 10) ** 3 + (i // 100) ** 3 == i:
#         print(f"{i}是水仙花数")

# a 百位数
# for a in range(1, 10):
#     # 十位数
#     for b in range(0, 10):
#         # 个位数
#         for c in range(0, 10):
#             if a**3+b**3+c**3 == a*100+b*10+c:
#                 print(a*100+b*10+c,'是水仙花数')

# a = 1
# d = 0
# while a < 10:
#     b = 0
#     while b < 10:
#         c = 0
#         while c < 10:
#             if (a ** 3) + (b ** 3) + (c ** 3) == int(f"{a}{b}{c}"):
#                 d += 1
#                 print(f'{a}{b}{c}')
#             c += 1
#         b += 1
#     a += 1
# print(f'{d}')

# 5. 百钱百鸡，公鸡5块钱1只，母鸡3块钱1只，小鸡1块钱3只，请问用100块钱买100只鸡，有多少种购买方法？
# 假设
# a 用来表示公鸡的数量
# for a in range(0, 21):
#     # b 来表示母鸡的数量
#     for b in range(0, 34):
#         # c 小鸡的数量
#         for c in range(0, 101):
#             if a + b + c == 100 and a * 5 + b * 3 + c / 3 == 100:
#                 print(f"公鸡的数量是{a}，母鸡的数量是{b}，小鸡的数量是{c}")
# #
# for gj in range(1,21):
#     for mj in range(1,34):#假设都买母鸡
#         xj = 100 - gj -mj # 小鸡的数量等于 100减去公鸡减去母鸡
#         if xj % 3 == 0 and gj * 5 + mj * 3 + xj // 3 == 100:
#             print(gj,mj,xj)
# # #
# for a in range(0,21):
#     for b in range(0,34):
#         for c in range(0,101):
#             if a + b +c == 100 and a * 5 + b * 3 + c / 3 == 100:
#                 print(f'公鸡数量是{a},母鸡数量是{b},小鸡数量是{c}')

# d=0
# for a in range(0,21):
#     for b in range(0,34):
#         c=(100-a-b)
#         if  c % 3 == 0 and 5*a+3*b+c/3 == 100:
#             d += 1
# print('共有',d,'种')


# a = 0
# f = 0
# while a <= 100:
#     d = 0
#     while d <= 100:
#         c = (100 - a)
#         while c >= 0:
#             if (d * 3) + (c * (1/3)) + (a * 5) == 100:
#                 print(f'{a}  {d}  {c}')
#                 f += 1
#             c -= 1
#             d += 1
#     a += 1
# print(f'{f}')

# 2.使用代码完成一下逻辑，根据输入的行数打印如下图案
# 请输入需要打印的行数：5
# *
# ***
# *****
# *******
# *********

# for i in range(1,6):
#     for j in range(1,i*2):
#         print("*",end="")
#     print()


# 4: 请用嵌套for循环输出如下等边三角形（三个边均是5个*）
# # @@@@@@*
# # @@@@@* *
# # @@@@* * *
# # @@@* * * *
# # @@* * * * *

# for i in range(5):
#     print("@" * (4 - i), end="")
#     print(" * " * (i + 1))
for i in range(5):
    for a in range(0,5-i):
        print("@",end="")
    for j in range(2*i+1):
        print("*" ,end="")
    print()



