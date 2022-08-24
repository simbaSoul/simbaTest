# 语法
"""
def 函数名(参数列表):
    return ....
"""


def play():
    a = 1
    b = 2
    return a, b
    # return [1, 2]


# 如果函数有返回值   那么尽量使用变量来接收返回值
num = play()
print(num)
print(type(list(num)))

