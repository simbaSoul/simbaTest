# 1. 请将“hello world”中的空格去除掉。
# 不可变数据类型
# s = "hello world"
# replace()  替换  指定的子串替换成另外的子串
# s1 = s.replace(" ", "")
# print(s1)
# 循环
# s1 = ""
# for i in s:
#     # 判断当前遍历到的字符是否是空格，如果是空格，跳过本次循环
#     if i.isspace():
#         continue
#     else:
#         # 如果不是空格，那么就和空字符串拼接   字符串的+号是拼接
#         s1 += i
# print(s1)

# 2. 输入三个整数x,y,z，请把这三个数由小到大输出。
# l = []
# for i in range(3):
#     l.append(eval(input("请输入数字:")))
# l.sort()
# print(l)

# a = 30
# b = 20
# c = 40
# if a > b:
#     if b > c:
#         print(c, b, a)
#     elif c > b:
#         if a > c:
#             print(b, c, a)
#         elif a < c:
#             print(b, a, c)


# 3. 定义一个列表，并插入一些数据，将其中非数值型的数据全部删除。
# l = [1, 2, 3, 4, "a", "b", "c", "d"]
# # l1 用来保存非数值型的字符串
# l1 = []
# for i in l:
#     # not 用来取反， 非数值型的字符串调用isdigit方法返回的是False 如果想要执行下方缩进的代码，那么就必须让False变为True
#     if not isinstance(i, (int, float)):
#         l1.append(i)
# for i in l1:
#     l.remove(i)
# print(l)

# 4. 定义一个函数，接收一个字符串和一个列表，将字符串拆分并追加到列表当中。
# def func4(a, b):
#     b.extend(a)
#     print(b)
# func4("abc", [1, 2, 34])


# 5. 定义一个单词，将奇数位的字母全部大写，偶数位的字母全部小写。
# 奇数位 1 3 5    偶数位 2 4 6
# w O r L d
# 1 2 3 4 5  顺序
# 0 1 2 3 4  索引
# w = "world"
# # # print(w[0].upper())
# w1 = ""
# # # 通过range+len 遍历当前字符串的索引
# for i in range(len(w)):
#     # 奇数位的数据对应的反而是偶数的索引
#     if i % 2 == 0:
#         w1 += w[i].upper()
#     else:
#         w1 += w[i].lower()
# print(w1)


# 6. 定义列表 [“hello”, “world”, “yoyo”]，如何把列表里面的字符串联起来，得到字符串 “hello_world_yoyo”？
# l = ["hello", "world", "yoyo"]
# join()
# s = "_".join(l)
# print(s)


# 7. 给定字符串“12345”，有几种方式将其倒序输出
# s = "12345"
# 切片
# print(s[::-1])
# s1 = ""
# 倒着取索引
# for i in range(len(s)-1, -1, -1):
#     s1 += s[i]
# print(s1)


# 8. 请输出1-2+3-4...-100的结果
# sum = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         sum -= i
#     else:
#         sum += i
# print(sum)


# 9. 建立一个包含10个字符的字符串A，然后对该字符串进行如下操作：
#   （1）计算输出字符串的长度；
# a = "12345abcde"
# print(len(a))

#   （2）从第1个字符开始，每间隔2个字符取1个字符，组成子字符串B；
# print(a[::2])
#   （3）将字符串A倒过来重新排列产生新的字符串C；
# print(a[::-1])


# 10. 编写程序提示用户输人一个在1到15之间的整数，然后显示一个金字塔
# number = int(input("请输入数字:"))
# i表示行  0 1 2
# for i in range(0, 3):  #3
#     for k in range(3 - i, 0, -1):
#         print(" ", end=" ")
#     for j in range(-i, i + 1):
#         print(abs(j) + 1, end=" ")
#     print()
