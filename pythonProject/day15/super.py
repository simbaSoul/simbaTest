class chushi():

    def __init__(self, name):
        self.name = name
        self.cai = "鱼香肉丝"

    def cook_cai(self):
        print(f"{self.name}拿手菜是{self.cai}")


class chushi2():

    def __init__(self, name):
        self.name = name
        self.cai = "土豆丝"

    def cook_cai(self):
        print(f"{self.name}拿手菜是{self.cai}")


class TuDi(chushi, chushi2):

    def __init__(self, name):
        self.name = name
        self.cai = "溜肉段"

    def cook_cai(self):
        print(f"{self.name}拿手菜是{self.cai}")

    def other_cai(self):
        # super 用来动态的去查找当前类的第一顺位的父类
        super().__init__(self.name)
        super().cook_cai()

        # chushi.__init__(self, self.name)
        # self.cook_cai() # self wss wss.name = 王姗姗  cai = 鱼香肉丝


wss = TuDi("王姗姗")  # wss.name = 王姗姗  wss.cai = 溜肉段
wss.other_cai()