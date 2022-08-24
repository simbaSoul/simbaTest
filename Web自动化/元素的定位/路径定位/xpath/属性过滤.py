import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://shop-xo.hctestedu.com/")
time.sleep(3)

# 下面这个语句执行完会返回一个元素（元素的对象）
# ele = driver.find_element("css selector", "html>body>div>div>div>form>div>input")
ele = driver.find_element("xpath", '//*[@id="doc-topbar-collapse"]/ul/li[3]/a[@class="am-dropdown-toggle "]') # 表示 前面有多少路径我都忽略，我从input开始查找


ele.screenshot("xpath_selector_属性过滤.png")