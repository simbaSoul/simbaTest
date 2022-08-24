import time

from selenium import webdriver

a = webdriver.Chrome()
a.get("http://www.baidu.com") #打开百度
time.sleep(5)   # 进程休眠
a.refresh() # 刷新
