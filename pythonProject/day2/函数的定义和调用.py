# 函数必须先定义  再调用  函数如果只是定义 而没有调用  那么解释器在执行代码的时候 但是并不会去执行函数内的代码

# 定义

# def func1(word):
#     print(word)
#
# # 调用
# func1("123")

def eat():
    print("干饭")


print("早上八点钟")
eat()
print("中午十二点")
eat()
print("晚上七点钟")
eat()