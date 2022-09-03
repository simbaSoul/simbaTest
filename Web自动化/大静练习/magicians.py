# magicians = ['alice','david','carolina']
# for magician in magicians:
#     print(magician)
# print(f"{magician.title()}，that was a great trick!")
# print(f"I can't wait to see your next trick,{magician.title()}.\n")
# print("Thank you，everyone.That was a great magic show!")


# massage = "Hello Python world"
# print(massage)

# pisas = ['liulianpisa','laroupisa','jituipisa']
# for pisa in pisas:
#     print(pisa)
# print(f"{pisa.title()},I like pepperoni pisa.")
# print(f"I really love pisas")

# a = []
# for i in range(1,11):
#     b = i ** 2
# a.append(i ** 2)
# print(a)

# a = [i ** 2 for i in range(1,11)]
# print(a)


# digits = [1,2,3,4,5,6,7,8,9,0]
# print(min(digits))
# print(max(digits))
# print(sum(digits))

# 打印1~20的数字
# for j in range(1, 21):
#     print(j)

# 创建1-1百万的列表 并打印出来 并统计最大值 最小值 和求和
# b = []
# for i in range(1,1000001):
#     b.append(i)
# print(min(b))
# print(max(b))
# print(sum(b))

# 打印奇数位
# a = []
# for i in range(1,21):
#     if i % 2 != 0:
#         a.append(i)
# print(a)
# 指定三位参数创建列表 并打印奇数位
# a =list(range(1,21,2))
# print(a)


# 打印3的倍数
# b = []
# for i in range(1,31):
#     if i % 3 == 0:
#         b.append(i)
# print(b)

# 创建列表并打印3的倍数
# a =list(range(3,31,3))
# print(a)

# 创建新列表 并打印立方
# a = []
# for i in range(1,11):
#     a.append(i ** 3)
# print(a)

# 立方解析
# a = [i ** 3 for i in range(1,11)]
# print(a)


# 切片
# players = ['a', 'b', 'c', 'd', 'e']
# print(players[0:3])
# print(players[1:4])
# print(players[:4])
# print(players[3:])
# print(players[-3:])
# for i in players[:3]:
#     print(i)

# 复制列表
# a = [1, 2, 3, 4, 5, 6]
# b = a
# a.append(7)
# b.append(8)
# print("my favorite foods are:")
# print(a)
# print("\nmy friend's favorite foods are:")
# print(b)


#   切片练习
# a = "The first three items in the list are:"
# print(a[0:15])

# 元组
# a = (100, 200)
# print(a[0])
# print(a[1])
# 自助餐练习
# a = ('披萨','榴莲','鸡腿','火腿','莎拉')
# for i in a:
#     print(i)
#
# a = ('腊肠','鸡蛋')
# for i in a:
#     print(i)

# if语句

# a = ['audi', 'bmw', 'subaru', 'toyota']
# for i in a:
#     if a == 'bmw':
#         print(i.upper())
#     else:
#         print(i.title())
#
# age = 19
# if age >=18:
#     print("haobang")
#     print("jiayou")

# age = 17
# if age >= 18:
#     print("haobangya")
# else:
#     print("对不起，年龄不符")

# age = int(input("请输入你的年龄："))
# if age < 4:
#     print("四岁以下免费")
# elif age < 18:
#     print("收费25元")
# else:
#     print("收费40元")

a = ['green']
# for i in a:
#     if i == 'bull':
#         print("玩家获得分5")
#     else:
#         print()
for i in a:
    if i =='green':
        print("玩家获得5分")
    if i != 'green':
        print("玩家获得10分")
    else:
        print("玩家获得15分")