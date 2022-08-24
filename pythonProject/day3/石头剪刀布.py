# 两个玩家  电脑  用户
# 用数字来代替石头剪刀布  石头---0  剪刀---1  布---2
# 用户的数字由自己输入  电脑的随机生成  暂时先写死
import random

player = int(input("玩家请出拳:"))
computer = random.randint(0, 2)  # 石头

# 玩家获胜
# 假设玩家的数字是0（石头） 那么电脑必须是1（剪刀）  玩家是1（剪刀）  电脑是2（布) 玩家是2（布） 电脑是0（石头）
# or 只要有一个表达式为True 那么结果就是True  只有都为False的时候 结果才是False
# and 表达式都为True的时候 结果才是True  只要有一个False  那么结果就是False
if (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
    print(f"电脑出的是{computer}，玩家获胜了")
elif computer == player:
    print("平局")
else:
    print(f"电脑出的是{computer}，电脑获胜了")



# 先来判断玩家获胜的情况
# 电脑出的是石头  玩家出什么能赢石头？  布  ---  2
# if player == 2:
#     print("电脑出的是石头，玩家出的是布，玩家获胜了")
# # 判断平局 玩家出的也是石头  石头 --- 0
# elif player == 0:
#     print("电脑出的是石头，玩家出的是石头，平局")
# else:
#     print("电脑出的是石头，玩家出的是剪刀，电脑获胜了")

