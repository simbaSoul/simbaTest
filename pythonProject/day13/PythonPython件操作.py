# r+ 用于文件的读写（r只能读）  文件指针放在了文件的开头  当写入数据的时候  会从开头开始  把原内容逐个覆盖 直到内容全部写入
# w+ 用于文件的读写（w只能写）   其他特性保持不变 就是多了个读的功能

file = open(r"dir1.mp3.txt", "a+", encoding="utf-8")
# file.seek(2, 0)
file.seek(0, 0)
print(file.read())

# print(file.readline())
# print(file.readline())
# print(file.readline())
