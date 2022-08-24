import time

from selenium import webdriver
driver = webdriver.Chrome()

driver.get("http://www.baidu.com")
time.sleep(3)   # 让人工操作新建一个标签页，
driver.close()  #关闭标签页，关闭的是driver实例对应的标签页
#   这个脚本 如果你么有人工的操作新建标签页，就会出现进程中会有残留的chrome浏览器