name = "马化腾"
id = 1
money = 6.66

# 我是马化腾，编号为001，银行卡余额6.66元

# 1. 格式化符号
print("我是%s, 编号为00%s, 银行卡余额为%s元" % (name, id, money))
# 2. format
print("我是{}, 编号为00{}, 银行卡余额为{}元".format(name, id, money))
# 3. f""
print(f"我是{name}, 编号为00{id}, 银行卡余额为{money}元")
