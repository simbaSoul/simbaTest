# 1. 生成一个10个随机数字的列表，表中为1~100之间的数字，将其中所有的两位数的十位数字相加，求最后的结果
import random

# l = []
# # range() 用来生成一个数字区间  range(10) 0~9  range(1,10) 1~9
# for i in range(10):
#     # 每一次循环都添加一个随机数
#     l.append(random.randint(1, 100))
# # 循环结束，列表当中应该有10个数字
# print(l)
# # 接下来开始对列表进行循环遍历， 每一次遍历都能获取到一个数字，但是，首先应该对当前数字进行是否是两位数的判断
# sum = 0
# for i in l:
#     # 将数字先转化为字符串类型  然后统计长度  长度为2  说明是两位数
#     if len(str(i)) == 2:
#         print(i)
#         sum += i // 10
# print(sum)


# 2. 有字符串“深情款款谁比我，爱意浓浓佳人喜。痴心最是搏颜欢，春风十里不如你”，请获取“我喜欢你”四个字。
def func2(s):
    # 现根据。进行切割
    s_l = s.split("。")
    # print(s_l)
    str = ""
    for i in s_l:
        s_l2 = i.split("，")
        # print(s_l2)
        for j in s_l2:
            str += j[-1]
    print(str)

    # 首先对字符串的。替换为，
    s1 = s.replace("。", "，")
    # print(s1)
    l = s1.split("，")
    # print(l)
    str = ""
    for i in l:
        str += i[-1]
    print(str)


# func2("深情款款谁比我，爱意浓浓佳人喜。痴心最是搏颜欢，春风十里不如你")
# 3. 有列表["悟空"，“牛魔王”，“八戒”，“蜘蛛精”，“沙僧”，“白骨精”]，请根据字符串的长度对列表中的数据进行分组。
def func3(l):
    l1 = []
    l2 = []
    for i in l:
        if len(i) == 2:
            l1.append(i)
        else:
            l2.append(i)
    print(l1)
    print(l2)


# func3(["悟空", "牛魔王", "八戒", "蜘蛛精", "沙僧", "白骨精"])

# 4. 生成一个10个随机数字的列表，表中为1~100之间的数字，请统计偶数有多少个，奇数有多少个。
# l = []
# # range() 用来生成一个数字区间  range(10) 0~9  range(1,10) 1~9
# for i in range(10):
#     # 每一次循环都添加一个随机数
#     l.append(random.randint(1, 100))
# print(l)
# # 用i来保存偶数的数量
# num = 0
# for i in l:
#     if i % 2 == 0:
#         num += 1
# print(f"偶数的数量是{num},奇数的数量是{10-num}")


# 5. 设计一个函数，定义一个初始用户名和密码，并且接收一个用户名和密码，判断用户名和密码是否正确，
# 如果用户名和密码正确，则成功登录，超过三次登录失败，则不允许再次登录。
def fun5():
    count=3
    for i in range(3):
        name = input("请输入用户名：")
        password = input("请输入用户密码：")
        if (name == 'admin') and (password == '123456'):
            print('登录成功')
            break
        else:
            count=count-1
            print('用户名或密码错误，请重新输入，还有',count,'次机会')
    else:
           print('超过三次，登录失败,不允许登陆，账号已冻结')


# fun5()


# a = "1"
# b = input("输入：")
# # 判断a和b是否相等  数字和数字  字符串   ==
# # 第一步 保证进行判断的数据  他们的数据类型相同
# if a == b:

