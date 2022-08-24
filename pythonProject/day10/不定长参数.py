# # 不定长参数用于在不确定函数会接收多少个参数的时候  进行使用  *args
def user_info(*args, **kwargs):
    print(args)
    print(kwargs)


# user_info('张三', 20, name='TOM', age=20, gender='男')

def fun(a, *args, **kwargs):
    print(a)
    print(args)
    # show(args) # 直接传递args相当于把元组作为整体传递了
    show(*args) # *args就是把元组解包


def show(a, b, c, d):
    print(a, b, c, d)


fun(1, 2, 3, 4, 5)


# def test1(a):
#     print(a)
#
#
# test1( (1, 2, 3) )

def func(a, b, c, *args, d=1, e=2, **kwargs):
    print(a, b, c)
    print(args)
    print(d, e)
    print(kwargs)


# func(10, 20, 30)


