import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://shop-xo.hctestedu.com/")
time.sleep(3)

# 下面这个语句执行完会返回一个元素（元素的对象）
ele = driver.find_element("xpath", "html/body/div/div/div/form/div/input")


ele.screenshot("xpath.png")