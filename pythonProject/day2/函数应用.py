# 打印一条横线
def print_line():
    print("-" * 50)


# print_line()

def three_num_avg(num1, num2, num3):
    """
    计算三个参数相加的结果
    :param num1:
    :param num2:
    :param num3:
    :return:
    """
    return (num1 + num2 + num3) / 3


print("三个数相加后的平均数是" + str(int(three_num_avg(10, 20, 30))))
