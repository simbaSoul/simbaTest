import time

from selenium import webdriver
from selenium.webdriver.common.by import By

d = webdriver.Chrome()  #driver 实例在运行代码过程中是标签的实例
d.get_screenshot_as_file("D:\PycharmProjects\Web自动化\imgs\打开浏览器.png")   # 截屏
d.get("http://www.baidu.com")
d.get_screenshot_as_file("D:\PycharmProjects\Web自动化\imgs\打开网址百度.jpg")
d.close()
d.get_screenshot_as_file("D:\PycharmProjects\Web自动化\imgs\关闭标签页.gif")   # 截屏不能实现 因为标签页关闭了
d.quit()
d.get_screenshot_as_file("D:\PycharmProjects\Web自动化\imgs\退出浏览器.raw")# 截屏不能实现 因为进程都销毁了更不能执行
#driver 实际上就是构建一个会话对象---> 标签页对象