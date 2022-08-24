# 上学 一周上3天  每天都要听5节课

# day 表示上学的天数
day = 1
while day <= 3:
    # myclass 用来表示每天的第几节课
    myclass = 1
    # 当循环发生嵌套的时候，内部循环执行完毕之后才会执行外部循环
    while myclass <= 5:
        print(f"这是第{day}天的第{myclass}节课")
        myclass += 1
    day += 1

# 当发生循环嵌套的时候，如果没有break和continue等关键字 那么程序依然按照正常顺序执行，
# 同时当进入到内部循环的时候，一定是先把内部循环执行完毕，才会回到外部循环
