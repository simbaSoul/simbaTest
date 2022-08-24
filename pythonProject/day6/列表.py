# 列表用来存储多个数据  列表采用的符号是[]  列表中的数据类型可以是不同的
# l = [1, 1.1, "a", True, [1, 2, 3], (1, 2, 3)]
# 列表是可变数据类型
#
l = [1, 3, 45, 56, 3]




#
# # 复制
# l1 = l.copy()
# print(l1)


# 判断
# in    if 数据 in 序列   用来判断数据序列当中是否包含了指定的数据
# if 1 not in l:
#     print("True")


# 查

#  index  返回指定数据在列表中的下标
# print(l.index(3, 2, 3))

# count 统计数据在列表中出现的次数
# print(l.count(1))

# len() 统计列表本身的长度 也就是列表中数据的数量
# print(len(l))


# 下标
# print(l[0])
# print(l[1])
# print(l[2])
# print(l[3])
# print(l[4])


# 改
# sort()  默认对序列进行正序的排序
# l.sort(reverse=True)
# print(l)


# reverse() 反转列表中的数据
# l.reverse()
# print(l)


# 通过下标来修改数据
# l[0] = "hello"
# print(l)


# 删
# clear 清空列表所有的数据
# l.clear()
# print(l)

# remove()  删除匹配内容的第一项
# l.remove(2)
# print(l)


# pop()  删除指定下标的数据  默认删除最后一个  同时也会返回被删除的数据
# r1 = l.pop(1)
# print(r1)
# print(l)


# del  并不是列表独有的方法  而是python自带的关键字
# 删除整个列表
# del l
# 删除列表中的某些数据
# del l[0]
# print(l)

# 增
# append  在列表的结尾追加数据
# l.append("沈利宁")
# append方法在原列表中追加数据序列的时候  数据序列会被当做整体来看待，而不会进行拆分
# l.append([1, 2, 3])
# print(l)

# extend  在列表的结尾追加数据  但是  如果追加的数据是序列，那么会把序列中的数据依次存储到列表当中
# l.extend([1, 2, 3])
# l.extend("侯培")

# insert  将指定的数据插入到指定的下标处  需要传递两个参数 参数1是下标位置 参数2是要插入的数据
# l.insert(0, "没交作业的潘文浩")
# print(l)



