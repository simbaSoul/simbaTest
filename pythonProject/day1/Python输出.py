name = "志超哥哥"
age = 30
weight = 75.5
stu_id = 1
stu_id2 = 1000


# f  语法  f"字符串{变量名}"
print(f"我的名字是{name},年龄是{age},体重是{weight}")


# format
# 语法：   字符串.format(变量名)
# print("我的名字是{},年龄是{},体重是{}".format(name, age, weight))


# 想要在字符串当中引用变量的值，需要使用格式化符号
# print("我的名字叫name")
# 语法  '格式化符号' % 变量名
# print("我的名字叫%s" % name)
# print("我的年龄是%d" % age)
# print("我的" % weight)

# print("我的学号是%d" % stu_id)
# print("我的学号是%3d" % stu_id)
# print("我的学号是%03d" % stu_id)
# print("我的学号是%-3d" % stu_id)
# print("我的学号是%03d" % stu_id2)

# print("我的名字叫%s,年龄是%s,体重是%s公斤" % (name, age, weight))


