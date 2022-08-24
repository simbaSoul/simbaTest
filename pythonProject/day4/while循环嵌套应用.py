# 1. 打印正方形的星号
# 打印5次，每次打印1行星星
# i = 1
# while i <= 5:
#     print("*  " * 5)
#     i += 1

# 设置一个变量 来表示行数
# line = 1
# while line <= 5:
#     # 设置一个变量，来表示每行星星的数量
#     star = 1
#     while star <= 5:
#         print("*", end="  ")
#         star += 1
#     print()
#     line += 1

# 打印三角形的星号  规律  每一行星星的数量  就是当前的行数
# line = 1  # 行数
# while line <= 5:
#     print("*" * line)
#     line += 1

# 循环嵌套的写法
line = 1
while line <= 5:
    # 星星的数量
    star = 1
    while star <= line:
        print("*", end="")
        star += 1
    print()
    line += 1


