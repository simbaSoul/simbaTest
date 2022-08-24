class Patato():
    def __init__(self):
        self.time = 0
        self.status = '生的'

    def Bbq(self, time):
        """
        烤地瓜方法
        :param time: 0-3分钟：生的，3-5分钟：半生不熟，5-8分钟：熟的
        :return:
        """
        self.time += time
        if self.time > 0 and self.time < 3:
            self.status = "生"
        elif self.time >= 3 and self.time < 5:
            self.status = "半生不熟"
        elif self.time >= 5 and self.time <= 8:
            self.status = "熟"
        elif self.time > 8:
            self.status = "烤糊"

    def __str__(self):
        return f"地瓜考了{self.time}分钟,{self.status}的"


dg = Patato()
dg.Bbq(1)
print(dg)
dg.Bbq(2)
print(dg)
dg.Bbq(2)
print(dg)
dg.Bbq(4)
print(dg)
