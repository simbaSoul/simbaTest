# 预算200的情况下  吃个什么自助呢？
money = int(input("请输入你本次周末happy的预算:"))

if money <= 200:
    print("吃个自助吧")
    # 此时对于自助的预算，进行二次的判断
    if money < 100:
        print("吃饱就行了")
    elif 100 <= money <= 150:
        print("稍微吃一点点海鲜")
    else:
        print("年轻人，不要委屈自己，吃好就行")
else:
    print("洗脚！喊上志超哥哥洗脚！！！")

