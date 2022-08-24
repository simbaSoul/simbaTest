# 局部变量  指的是函数体内的变量
# 全局变量  函数体内外都能访问的变量
a = 100


def testA():
    print(a)


def testB():
    # 就近原则
    global a
    a = 200
    print(a)


testB()
testA()


def test1():
    return 50


def test2(num):
    print(num)


# result = test1()
# test2(test1())

