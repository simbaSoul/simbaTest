# 定义一个文件操作类，并定义若干子类，要求通过传递不同的子类对象，来实现不同的文件操作方法，
# 如子类一可以实现复制，子类二可以实现按行读取等等，具体功能自定义即可。
import os


class FileCZ():
    def operate(self):
        pass


class Cp(FileCZ):
    def __init__(self, file_name):
        self.file_name = file_name

    def operate(self):
        file_name = open(self.file_name, 'r')
        new_file = open((self.file_name + '[备份]'), 'w+')
        new_file.write(file_name.read())
        file_name.close()
        new_file.close()

class Wr(FileCZ):
    def __init__(self, file_name):
        self.file_name = file_name
    def operate(self):
        file_name = open(self.file_name, 'r')
        content =  file_name.readline()
        print(f'第一行：{content}')
        content = file_name.readline()
        print(f'第二行：{content}')
        file_name.close()

class Per():
    def cz(self, fileCz):
        fileCz.operate()


c = Cp('123.txt')

w = Wr('123.txt')
p = Per()
p.cz(w)
