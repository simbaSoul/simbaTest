from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait

from 华测商城.common import random_


def user_register(dr, time_out, cz):
    """
     注册
    :param dr: 浏览器实例
    :param time_out: 等待时间
    :param cz: 操作方式
    :return: 元素对象
    """
    element = Wait(dr, time_out).until(EC.presence_of_element_located(cz))
    return element


driver = webdriver.Chrome()

driver.get("http://shop-xo.hctestedu.com/")

element_locate = (By.LINK_TEXT, "注册")
resister_btn = user_register(driver, 3, element_locate)
resister_btn.click()

password = username = random_.time_ran()

# 输入用户名
user_info = (By.NAME, "accounts")
user_info_ele = user_register(driver, 3, user_info)
# user_info_ele = Wait(driver, 3).until(EC.presence_of_element_located(user_info))
user_info_ele.send_keys(username)

# 输入密码
password_info = (By.NAME, "pwd")
password_info_ele = user_register(driver, 3, password_info)
# password_info_ele = Wait(driver, 3).until(EC.presence_of_element_located(password_info))
password_info_ele.send_keys(password)

# 点击注册按钮
register_btn = (By.CLASS_NAME, "btn-loading-example")
register_btn_ele = user_register(driver, 3, register_btn)
# register_btn_ele = Wait(driver, 3).until(EC.presence_of_element_located(register_btn))
register_btn_ele.click()
