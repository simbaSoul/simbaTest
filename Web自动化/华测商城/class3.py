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
ele1 = user_register(driver, 3, element_locate)
ele1.click()

password = username = random_.time_ran()

# 输入用户名
user_info = (By.NAME, "accounts")
user_info_ele = WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(user_info))
user_info_ele.send_keys(username)

# 输入密码
password_info = (By.NAME, "pwd")
password_info_ele = WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(password_info))
password_info_ele.send_keys(password)

# 点击注册按钮
register_btn = (By.CLASS_NAME, "btn-loading-example")
register_btn_ele = WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(register_btn))
register_btn_ele.click()
