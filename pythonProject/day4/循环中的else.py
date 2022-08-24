# 循环中的else 表示当循环顺利执行完毕之后要执行的代码

# while
# i = 1
# while i <= 5:
#     if i == 6:
#         break
#     print("拼命学习")
#     i += 1
# else:
#     print("月薪过万")


# for
for i in range(1, 10):
    if i == 9:
        break
    print(i)
else:
    print("循环正常执行完毕")


