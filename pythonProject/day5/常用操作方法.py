# find(子串，[起始位置下标，结束位置下标])

# str = "moneyandmoney"
# str = "you jump,I jump,lsq jump"
# print(str)
# print(str.find("wo"))
# print(str.find("wo", 0, 3))
# print(str.rfind("money"))
# print(str.index("lhd"))
# print(str.count("neya"))

# 替换  replace(被替换的字符串，替换后的字符串，替换次数)
# 字符串是不可变数据类型 所以调用replace方法对原字符串进行替换之后，必须用变量接收，方便后续使用
# s1 = str.replace("money", "$", 1)
# print(s1)

# 切割，分隔  split  根据指定好的字符来对字符串进行切割
# 切割之后得到的是一个装载了切割后字符串的列表，而且，被切割的字符将不会显示在列表当中
# s = str.split(",")
# print(s)

# splitlines 按行切割  换行符\n
# print(str.splitlines())

# partition 和split类似 但是可以保留被切割的字符  固定返回包含3个数据的元组  只会根据匹配到的第一个字符进行切割，后续不做处理
# s1 = str.partition(",")
# print(s1)  # ('you jump', ',', 'I jump,lsq jump')

# s = str.rpartition(",")
# print(s)

# l = ['a', 'b', 'c']
# s = "！！".join(l)
# print(s)

# str = "      hello world        ,          "
# capitalize  将字符串的首字母大写
# print(str.capitalize())
# print(str.title())
# print(str.lower())
# print(str.upper())

# print(str.lstrip())
# print(str.rstrip())
# print(str.strip())


# str = "hello"
# print(str.ljust(10, "~"))
# print(str.rjust(10, "~"))
# print(str.center(11, "~"))

# startswith  判断字符串是否以指定的单个字符或子串开头  是就返回True  不是就返回False
# 至少有一个字符  并且全部都是字母
str = 'hello'
# print(str.startswith("life"))
# print(str.endswith("fe"))


print(str.islower())


