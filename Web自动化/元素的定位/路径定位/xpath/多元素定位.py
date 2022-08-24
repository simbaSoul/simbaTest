import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://shop-xo.hctestedu.com/")
time.sleep(3)

# 下面这个语句执行完会返回一个元素（元素的对象）
els = driver.find_element(By.XPATH, '//*[@id="doc-topbar-collapse"]/ul') # 表示 前面有多少路径我都忽略，我从input开始查找
els.screenshot("ele.png") #多元素进行截图
els1 = els.find_elements(By.TAG_NAME,"a") #返回元素对象的list列表
for i in els1:
    print(i.get_attribute("text"))
