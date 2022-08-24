# 定义一个变量a
a = 1
while a <= 3:
    print(f"我是第{a}个a")
    b = 1
    while b <= 4:
        if b == 3:
            b += 1
            continue
        print(f"我是第{b}个b")
        b += 1
    a += 1