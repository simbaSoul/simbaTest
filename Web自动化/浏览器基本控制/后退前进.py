import time

from selenium.webdriver.common.by import By
from selenium import webdriver

a = webdriver.Chrome()

a.get("http://localhost:8080/login.action")
time.sleep(3)
a.find_element(by=By.ID,value=("usercode")).send_keys("admin")
a.find_element(by=By.ID,value=("userpassword")).send_keys("123456")
a.find_element(by=By.XPATH,value='/html/body/div[2]/form/input').click()
time.sleep(3)
# 如果我们需要回到百度，我们就需要后退
# a.back()    # 后退
# time.sleep(3)
# a.forward() # 前进
print("登录成功！")
# a.quit()    # 关闭浏览器