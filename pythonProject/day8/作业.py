# 1. 现有字符串“我本三山客，喜探四海花，欢心今常驻，你与影共斜”，请定义函数，提取“我喜欢你”，即每句诗的首个字符。
# def i(a):
#    b=a.split('，')
#    for c in b:
#        print(c[0],end='')


# i("我本三山客，喜探四海花，欢心今常驻，你与影共斜")


# # 2. 定义一个函数，接收包含任意数据的列表，将列表内的数字全部修改为原数字的立方。
# def func2(l):
#     for i in l:
#      if isinstance(i,int):
#          l[l.index(i)]=i**3
#     print(l)
# func2([2, 2, 2, "a", "b", "c"])

# def func2(l):
#     for i in l:
#         if isinstance(i,int):
#             a = l.index(i)
#             l[a] = i ** 3
#     print(l)
# func2([1,2,3,4,"wwww"])

# 3. 定义一个函数，生成一个手机号，规则简化为手机号以1开头，第2位不能是0，1，2。
# str()  int()  float()  eval()   list() tuple()  set()
import random


def func3():
    # 手机号是11位的
    # 通过一个11次的循环 每1次循环生成一个数字  并且把所有的数字保留并组合成手机号
    # 手机号的第1位  是1
    # 手机号的第2位  不能是0  1  2
    # 其他位随意
    phone = ""  # "1"
    for i in range(1, 12):
        # 第一次循环  i的取值是1  1刚好是手机号的第1位 所以把i的值保留就可以
        if i == 1:
            phone += str(i)
        # 循环到第2次的时候  需要生成一个3~9之间的随机数
        elif i == 2:
            num = random.randint(3, 9)
            phone += str(num)
        else:
            num1 = random.randint(0, 9)
            phone += str(num1)
    print(phone)


# func3()


# 4. 请生成一个长度为10的数字列表，并统计奇数位的数字的和。
def func4():
    l = []
    # 当列表的长度小于11的时候
    while len(l) < 10:
        num = random.randint(1, 100)
        l.append(num)
    print(l)
    result = 0
    for i in range(len(l)):
        # 偶数位的索引 对应的 刚好是奇数位的数据
        if i % 2 == 0:
            print(l[i])
            result += l[i]
    print(result)


# func4()

# 索引  序列  用来表示序列中数据的位置  参考车票
# 索引 从0开始  依次递增   最大值等于当前序列的长度减1
# s = "abcdefg"
# 根据索引取值的方法  序列的名称[索引值]
# s1 = "a".replace("a", "")
# print(s1)


# 5. 请计算1+2-3+4+5-6+..-12-13+14-15...-30-31..+100的结果。  逢3减  3的倍数 或者说  带3（个位为3或十位为3的）  减去

# r = 0
# for i in range(1, 101):
#     # if i % 3 == 0 or "3" in str(i):
#     if i % 3 == 0 or i % 10 == 3 or i // 10 == 3:
#         r -= i
#     else:
#         r += i
# print(r)


# 企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？

def func(money):
    """

    :param money: 利润
    :return:
    """
    # 利润(I)低于或等于10万元时，奖金可提10%；
    if money <= 100000:
        mymoney = money * 0.1
    # 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
    # 当利润超过10万的时候  有两种提成方式  会有两部分奖金
    # 低于10万的  10%  100000 * 0.1 = 10000
    # 高于10万的  7.5%  20000 * 0.075 =
    elif 100000 < money < 200000:
        mymoney = 100000 * 0.1 + (money - 100000) * 0.075
    # 20万到40万之间时，高于20万元的部分，可提成5%
    # 220000  100000  10%  100000 7.5%  20000 5%
    elif 200000 <= money < 400000:
        mymoney = 100000 * 0.1 + (money - 100000) * 0.075 + (money - 200000) * 0.05


# func(220000)


