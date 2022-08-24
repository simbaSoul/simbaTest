from day14.Furniture import Furniture


class Hourse():
    def __init__(self, address, area):
        self.address = address
        self.area = area
        self.shengArea = area
        self.furniture = []


    def rong(self, furniture):
        if self.shengArea >= furniture.area:
            self.furniture.append(furniture.name)
            self.shengArea -= furniture.area
        else:
            print("家具太大放不下")


    def __str__(self):
        return f"房子位于{self.address},占地面积{self.area},剩余面积{self.shengArea}"


hourse = Hourse('北京',30)
furniture = Furniture("沙发",20)
furniture1 = Furniture("床",20)
hourse.rong(furniture)
print(hourse)
hourse.rong(furniture1)