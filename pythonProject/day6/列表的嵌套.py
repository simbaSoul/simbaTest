# l = [1, 2, 3, 4, [5, 6, 7, [8, 9, 10]], "1"]
#
# l1 = l[4][3][1]
# print(l1)
#
l = [1, 2, 3, [4, 5, 6]]


# result = 0
# for i in l:
#     if isinstance(i, list):
#         for j in i:
#             result += j
# print(result)


print(isinstance("1", (int,  float)))
