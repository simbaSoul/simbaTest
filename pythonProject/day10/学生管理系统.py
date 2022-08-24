def add_student():
    """
    添加学员信息，学员的信息应该是存储在字典中的，而所有的字典都存储到列表中
    [{name:志超,age:20}, {name:启航,age:20}]
    :return:
    """
    # 根据学生的姓名来做重复性判断，所以应该在输入完姓名之后立马开始对当前存储学生信息的列表，进行遍历以及判断
    name = input("请输入学生的姓名：")
    # 因为列表中存储的是包含学生信息的字典  所以每一次遍历的i 都是一个字典
    for studict in stulist:
        if name == studict['name']:
            print("学生信息已存在，请勿重复添加！")
            break
    else:
        age = int(input("请输入学生的年龄："))
        sex = input("请输入学生的性别：")
        d = {}
        d['name'] = name
        d['age'] = age
        d['sex'] = sex
        stulist.append(d)
        print("学生信息添加成功！")


def del_student():
    """
    删除学生信息
    :return:
    """
    # 当用户输入要删除的学生的姓名之后  应该去列表当中匹配对应的学生信息
    del_name = input("请输入要删除的学生的姓名:")
    for studict in stulist:
        if del_name == studict['name']:
            stulist.remove(studict)
            print("学生信息删除成功!")
            break
    else:
        print("该学生不存在！")


def update_student():
    up_name = input("请输入要修改信息的学生的姓名:")
    for studict in stulist:
        if up_name == studict['name']:
            studict['age'] = eval(input("请输入修改后的学生的年龄:"))
            print("学生信息修改成功!")
            break
    else:
        print("该学生不存在！")


def select_student():
    select_name = input("请输入要查找的学生的姓名:")
    for studict in stulist:
        if select_name == studict['name']:
            print(f"学生的姓名是{studict['name']},年龄是{studict['age']},性别是{studict['sex']}")
            break
    else:
        print("该学生不存在！")


def select_all_students():
    if len(stulist) == 0:
        print("当前列表没有学生信息!")
    else:
        print("姓名\t年龄\t性别")
        for i in stulist:
            print(f"{i['name']}\t{i['age']}\t{i['sex']}")


def main_info():
    print('-' * 20)
    print('欢迎登录学员管理系统')
    print('1: 添加学员')
    print('2: 删除学员')
    print('3: 修改学员信息')
    print('4: 查询学员信息')
    print('5: 显示所有学员信息')
    print('6: 退出系统')
    print('-' * 20)

    num = eval(input("请输入功能序号(1~6)："))
    if num == 1:
        add_student()
    elif num == 2:
        del_student()
    elif num == 3:
        update_student()
    elif num == 4:
        select_student()
    elif num == 5:
        select_all_students()
    elif num == 6:
        print("欢迎使用，再见！")
        exit(0)
    else:
        print("输入有误，请重新输入！")


# 新建全局变量stulist 来存储学生的信息
stulist = []
while True:
    main_info()

print("姓名\t年龄\t性别")