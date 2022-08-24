# while 写法 1~100之间的和
# i = 1
# result = 0
# while i <= 100:
#     result += i
#     i += 1
# print(result)

# 通过for循环来求1~100之间的和
# range()  根据用户输入的数字，来生成一个对应的数字序列  序列的范围是从参数1到参数2的前一位
# for i in range(1, 11):
#     print(i)

# result = 0
# for i in range(1, 101):
#     result += i
# print(f"1~100之间的和是{result}")

for i in range(1, 4):
    if i == 2:
        print("拉肚子了")
        continue
    print(f"忠哥正在跑第{i}圈")
