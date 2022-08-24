# open(文件的路径（名称）, 模式)
# r 模式  只读模式
# w 模式  只要使用w模式打开文件 源文件内容全部被删除  如果打开的文件不存在  那么新建该文件
# a 模式 追加 指针会放在原内容的末尾  这样新的内容就会接着之前的内容继续写入
file = open(r"4.txt", "w", encoding="utf-8")
# file.write("\n中午吃个红烧肉")


# read() 读取文件内容
# print(file.read())
# write 向文件写入  只读模式不允许编辑
# file.write("hello")
# close 关闭文件


file.close()
