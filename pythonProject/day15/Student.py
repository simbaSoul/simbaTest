class Student():
    def __init__(self, name, sex, phone):
        self.name = name
        self.sex = sex
        self.phone = phone


    def __str__(self):
        return f"姓名：{self.name}，性别：{self.sex}"