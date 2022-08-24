# 位置参数  根据参数的顺序和位置来传递对应的数值

def user_info(name, age, gender="女"):
    print(f'您的名字是{name}, 年龄是{age}, 性别是{gender}')


# user_info('TOM', 20, '男')

# 关键字参数  传递实参的时候  不根据形参的顺序来传递  而通过指定形参的名称来传递值
# user_info(name='TOM', gender='男', age=20)
# 传参时  同时包含了位置参数和关键字参数  那么 位置参数必须在前面
# user_info('TOM', gender='男', age=20)

# user_info('TOM', age=20)


