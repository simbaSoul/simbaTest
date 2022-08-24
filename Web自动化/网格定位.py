"""
网格定位也叫相对定位（相对位置）
"""
import time

from selenium.webdriver.common.by import By
# 引用网格定位的包
from selenium.webdriver.support.relative_locator import locate_with, with_tag_name
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://shop-xo.hctestedu.com/")

time.sleep(3)

ele = driver.find_element(By.LINK_TEXT, "登录")
# 通过相对位置去定位 在登录元素 右边的 注册元素
# locate_with 中的参数用于过滤 元素的定位方式
# 右边
ele2 = driver.find_element(locate_with(By.TAG_NAME, "a").to_right_of(ele))
ele2.screenshot("注册元素.png")

# 左边
ele3 = driver.find_element(locate_with(By.TAG_NAME, "a").to_left_of(ele2))
ele3.screenshot("登录元素.png")

# 附近 有个范围 默认为50px
els4 = driver.find_element(with_tag_name("em").near(ele3))
els4.screenshot("logo.png")

driver.quit()

"""
下拉列表的定位 Select
"""
