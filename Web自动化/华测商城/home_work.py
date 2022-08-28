import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://shop-xo.hctestedu.com/")

located = (By.CLASS_NAME, "goods-list")
good_lists = Wait(driver, 3).until(EC.visibility_of_element_located(located))  # 定位商品列表
# print(len(good_lists))
located = (By.TAG_NAME, "a")
good_items = good_lists.find_elements(*located)  # 定位所有商品

ls = []
for i in good_items:  # 遍历商品并在新标签页打开
    if i.text != "":
        ls.append(i.text)
        i.click()
title = []
for j in range(len(driver.window_handles) - 1, 0, -1):  # 遍历标签页对象列表并加到title里
    driver.switch_to.window(driver.window_handles[j])
    title.append(driver.title)

for a in range(len(ls)):  # 判断打开的标签页名称 是否与window_handles对象列表一致
    if ls[a] == title[a]:
        print("打开正确~")

time.sleep(3)
driver.quit()
# 'http://shop-xo.hctestedu.com/index.php?s=/index/goods/index/id/10.html'
# 'http://shop-xo.hctestedu.com/index.php?s=/index/goods/index/id/11.html'
# 'http://shop-xo.hctestedu.com/index.php?s=/index/goods/index/id/9.html'
# 'http://shop-xo.hctestedu.com/index.php?s=/index/goods/index/id/3.html'
# 'http://shop-xo.hctestedu.com/index.php?s=/index/goods/index/id/1.html'
# 'http://shop-xo.hctestedu.com/index.php?s=/index/goods/index/id/2.html'
