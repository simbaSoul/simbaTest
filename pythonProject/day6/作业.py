# 1. 请通过代码生成一个随机5位数
import random

# print(random.randint(10000, 99999))

# s = ""
# for i in range(5):
#     s = s + str(random.randint( 1, 9))
# print(s)


# 2. 输入任意字符串，判断字符串中是否包含you这个单词，如果存在，请返回其开始位置下标以及结束位置下标，如果不存在，请给出提示
# s = "youandme"
# print(s.find('you'))
# print(s.find('you') + 2)

# s = input("请输入字符串:")
# if s.find("you") != -1:
#     print(f"you的开始位置下标是{s.find('you')}, you的结束位置下标是{s.find('you') + 2}")
# else:
#     print("字符串中不包含you")

# 3. 输入任意字符串，统计字符串中字母的数量，数字的数量，空格的数量以及其他字符的数量
# 保存字母的数量
# a = 0
# b = 0
# c = 0
# d = 0
# s = input("请输入字符串:")
# for i in s:
#     if i.isalpha():
#         a += 1
#     elif i.isdigit():
#         b += 1
#     elif i.isspace():
#         c += 1
#     else:
#         d += 1
#
# print(f"字母的数量是{a},数字的数量是{b},空格的数量是{c},其他字符的数量是{d}")

# 4. 求s= a + aa + aaa + … + aa…a 的值（最后一个数中 a 的个数为 n ），其中 a 是一个1~9的数字，例如： 2 + 22 + 222 + 2222 + 22222 （此时 a=2 n=5 ）
# a = 2
# sum = 0
# for i in range(5):
#     sum += a
#     a = a * 10 + 2
# print(sum)


# 5. 我国现有13亿人口，设每年增长0.8%，编写程序，计算多少年后达到26亿？
# p = 13
# year = 0
# while True:
#     if p >= 26:
#         break
#     p = p * (1 + 0.008)
#     year += 1
#
# print(year)

# 6. 求1~100之间能被7整除，但不能同时被5整除的所有整数
# for i in range(1, 101):
#     if i % 7 == 0 and i % 5 != 0:
#         print(i)

# 7. 有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
# for i in range(1, 5):
#     for j in range(1, 5):
#         for l in range(1, 5):
#             if (i != j) and (i != l) and (j != l):
#                 print(f"{i}{j}{l}")


# a = int(input("请输入一个加数a："))
# n = int(input("请输入一个相加次数n："))
# s = 0
# b = a
# for i in range(n):
#     s += a
#     a = a * 10 + a
# print(s)
