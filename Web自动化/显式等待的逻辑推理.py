import time


from selenium import webdriver






# 1.找不到元素出发NotFound
# 2.每次找到元素，应该有时间控制
# 3.找到元素，就不找了

driver = webdriver.Chrome()
Notfound = ""
by = ""
value = ""
default = True
default_time = time.time()
# 假设我们只等待3秒
while default:
    try:
        driver.find_element(by,value)
        default = False
    except Notfound:
        last_time = time.time()
    if last_time - default_time > 3:
        break


