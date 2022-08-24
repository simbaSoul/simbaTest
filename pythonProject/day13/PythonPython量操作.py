import os


dir = os.listdir()
print(dir)
for i in dir:
    """
        批量修改
    """
    new_name = 'Python' + i
    os.rename(i,new_name)
# flag = 2
# for i in dir:
#     if flag ==1 :
#         new_name = 'Python_' + i
#     elif flag ==2 :
#         num = len('Python-')
#         new_name = i[num:]
#     print(new_name)
#     os.rename(i,new_name)
