# 1. 定义函数，将指定目录下所有的文件全部重命名为test.txt。（考虑目录下有多层嵌套目录的情况）
# 2. 目录dir1下有若干文件，目录dir2下有若干文件，要求定义函数将两个目录下的文件位置互换。
import os


def common(dir1, dir2, file_lb):
    for i in file_lb:
        os.chdir(dir1)
        old_file = open(f"{i}", 'r+', encoding="utf-8")
        os.chdir(dir2)
        new_file = open(f"{i}", 'w+', encoding="utf-8")
        while True:
            content = old_file.read(1024)
            if len(content) == 0:
                break
            new_file.write(content)
        os.chdir(dir1)
        old_file.close()
        new_file.close()
        os.remove(i)


def jh(path1, path2):
    d2 = os.listdir(path2)
    d1 = os.listdir(path1)
    common(path1, path2, d1)
    common(path2, path1, d2)


jh('../dir1', '../dir2')


# 3. 定义汽车类，并自定义若干属性，要求最后打印对象名称能够看到所有属性。
class Car():
    def __init__(self, name, color, brand):
        self.name = name
        self.color = color
        self.brand = brand

    def __str__(self):
        return f"车主名字{self.name},汽车颜色是{self.color},汽车品牌是{self.brand}"


new_car = Car("贾静静的车", "白色", "劳斯莱斯")


# print(new_car)


# 4. 定义教室类，桌子类，椅子类，自定义教室，桌子，椅子的占地面积，请统计教室最多能放多少张桌子和椅子
class Class():
    def __init__(self, area, table, chair):
        self.area = area
        self.free_area = area
        self.table = table
        self.chair = chair

    def Content(self):
        for i in range(self.area // self.table.area):
            for j in range(self.free_area // self.chair.area):
                if (i * self.table.area + j * self.chair.area) == self.area:
                    print(f"桌子有{i}，椅子有{j}")


class Table():
    def __init__(self):
        self.area = 2


class Chair():
    def __init__(self):
        self.area = 1


table = Table()
chair = Chair()
c = Class(100, table, chair)
c.Content()


# 5. 定义学生类，要求学生的属性有姓名以及语文，数学，英语三门课的成绩，要求最后打印学生对象时，能够输出学生的姓名和最高分成绩以及最低分成绩。


class Student():
    def __init__(self, name, yuwen, shuxue, yingyu):
        self.name = name
        self.score = [{"语文": yuwen, "数学": shuxue, "英语": yingyu}]
        self.fs = [max(self.score[0].values()), min(self.score[0].values())]

    def __str__(self):
        return f"最高分是：{self.fs[0]},最低分是{self.fs[1]}"


# stu = Student("张三", 80, 90, 76)
# stu1 = Student("yiy", 6, 99, 76)
# print(stu,stu1)


def f(lb):
    for i in range(len(lb)):
        if isinstance(lb[i],int):
            lb[i] = lb[i] ** 2

l1 = ['123', 1, 3, 4, 5, 'sf']
f(l1)
print(l1)