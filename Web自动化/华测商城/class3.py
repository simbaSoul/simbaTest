import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with, with_tag_name
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from 华测商城.common import random_

"""
课后作业内容

不准使用强制等待
仅使用显性等待和隐性等待完成下面的流程脚本：
1：注册用户
2.新增的用户进行购物车添加商品的操作
3.对新增的用户进行个人信息的修改（仅修改性别和昵称）
4.将上述的三个步骤封装成函数
"""

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://shop-xo.hctestedu.com/")

driver.implicitly_wait(3)


def user_register(dr, time_out, cz):
    """
     注册
    :param dr: 浏览器实例
    :param time_out: 等待时间
    :param cz: 操作方式
    :return: 元素对象
    """
    element = WebDriverWait(dr, time_out).until(expected_conditions.presence_of_element_located(cz))
    return element


# 获取注册按钮 并点击
element_locate = (By.LINK_TEXT, "注册")
resister_btn = user_register(driver, 3, element_locate)
resister_btn.click()

password = username = random_.time_ran()

# 输入用户名
user_info = (By.NAME, "accounts")
user_info_ele = user_register(driver, 3, user_info)
# user_info_ele = WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(user_info))
user_info_ele.send_keys(username)

# 输入密码
password_info = (By.NAME, "pwd")
password_info_ele = user_register(driver, 3, password_info)
# password_info_ele = WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(password_info))
password_info_ele.send_keys(password)

# 点击注册按钮
register_btn = (By.CLASS_NAME, "btn-loading-example")
register_btn_ele = user_register(driver, 3, register_btn)
# register_btn_ele = WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(register_btn))
register_btn_ele.click()

good_list = driver.find_element(By.CLASS_NAME, "goods-list")
good_hrefs = good_list.find_elements(By.TAG_NAME, "a")
# for i in good_hrefs:
#     i.get_attribute("href")
# driver.get(good_hrefs[random.randint(0, len(good_hrefs) - 1)].get_attribute("href"))
driver.get("http://shop-xo.hctestedu.com/index.php?s=/index/goods/index/id/9.html")

theme_option = (By.CSS_SELECTOR, ".theme-options")  # 所有商品属性选项
theme_options = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_all_elements_located(theme_option))

for i in theme_options:
    if "sku-items" in i.get_attribute("class"):
        sku_color = (By.CSS_SELECTOR, "ul>li")
        sku_element = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_all_elements_located(sku_color))
        randint = random.randint(0, len(sku_element) - 1)
        sku_element[randint].click()



# print(len(div_list))

# sku_items = driver.find_element(By.XPATH,
#                                 '/html/body/div[4]/div[2]/div[2]/div/div[2]/dl/dd/div[2]/div[3]/form/div[1]/div[1]/ul')
# lis = sku_items.find_elements(By.TAG_NAME, "li")
# for i in range(len(lis)):
#     index = random.randint(0, 2)
#     lis[index].click()
