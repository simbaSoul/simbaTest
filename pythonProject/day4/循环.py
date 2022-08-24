# 志超跑步 最多3圈
# 循环变量的初始值
# 表示志超开始跑第一圈
# i = 1
# while i <= 100:
#     print(f"志超跑了第{i}圈")
#     i += 1

# 1~100之间的累加和  1 + 2 +3 +4 +5+ .. + 100     0 用来和1相加
# i = 1
# # 用 result 来接收并保存相邻两个数字相加的和
# result = 0
# while i <= 100:
#     result += i  # 用result 来保存数字相加的结果
#     i += 1
#     # print(result)
#
# print(f"1~100之间的和是{result}")


i = 1
result = 0
while i <= 100:
    # 对参与循环的数字i进行判断，判断它是不是偶数
    if i % 2 != 0:
        result += i
    i += 1


print(f"1~100之间奇数的和是{result}")


# i = 2
# result = 0
# while i <= 100:
#     result += i
#     # i += 2
#
#
# print(f"1~100之间偶数的和是{result}")
