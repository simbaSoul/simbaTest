a = 1
b = 2
c = 3
# and  只要有一个值为0，则结果为0，否则结果为最后一个非0数字
# and  只要有一个False  那么最终的结果就是False  只有表达式都为True的时候  结果才是True
# print((a > b) and (a < c))  # True and True

# or  只要表达式当中有一个True 那么最终的结果就是True  当所有的表达式的结果都是False的时候  最终的结果才是False
# print((a > b) or (a > c) or (b < a))

# not 非 取反
print(not (a > b))


