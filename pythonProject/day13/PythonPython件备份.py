# 1.用户输入目标文件 dir1.mp3.txt
old_name = input('请输入您要备份的文件名：')
# print(old_name)
# 2.规划备份文件的名字
# 提取后缀 -- 找到后缀前的. -- 名字和后缀分离 -- 最右侧的点才是后缀的点 -- 字符串查找某个字串rfind
index = old_name.rfind('.')
# print(index)
# 以.分割开原文件名并在修改后进行拼接 新名字 = 原名字 + [备份] + 后缀
# 使用切片[开始：结尾：步长]获取原文件名称和后缀
print(old_name[:index])
print(old_name[index:])
new_name = old_name[:index] + '[备份]' + old_name[index:]
print(new_name)
# 3.备份文件写入数据(确保数据和源文件一样)
old_f = open(old_name,'rb')
new_f = open(new_name,'wb')
# 如果不确定目标文件大小，循环读取写入，当读取出来的数据为空则终止循环
while True:
    content = old_f.read(1024)
    if len(content) == 0:
        break
    new_f.write(content)
# 4.关闭文件
old_f.close()
new_f.close()