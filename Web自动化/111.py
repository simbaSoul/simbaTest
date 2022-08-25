# -*- coding: utf-8 -*-
# author: 华测-长风老师
"""
课后作业内容：
不准使用强制等待
仅使用显性等待和隐性等待完成下面的流程脚本：
1、注册用户（脚本可重用，意味着你的用户名需要构建一个随机字符）
2、对新增的用户进行购物车添加商品的操作
3、对新增的用户进行个人信息的修改（仅修改性别和昵称）
4、将上述的三个步骤封装成函数
"""

from selenium import webdriver
import time
import random


# 1、注册用户（脚本可重用，意味着你的用户名需要构建一个随机字符）

def registered(driver, username, password):
    driver.find_element("link text", "注册").click()
    # username = password = f"test_{str(time.time()).replace('.', '')[5::]}"
    driver.find_element("name", "accounts").send_keys(username)
    driver.find_element("name", "pwd").send_keys(password)
    driver.find_element("css selector", ".am-btn-block").click()


# 2、对新增的用户进行购物车添加商品的操作

def add_goods_to_cart(driver):
    # driver.find_element("css selector", ".goods-images").click()  # 对一个商品的点击 使用find_element 永远得到的是第一个商品
    random.choice(driver.find_elements("css selector", ".goods-images")).click()  # 对一个商品的点击 使用find_elements 随机选择商品

    handles = driver.window_handles

    driver.switch_to.window(handles[-1])

    format_ul = driver.find_elements("css selector", ".sku-items>ul")

    if format_ul:
        for i in format_ul:
            format_li = i.find_elements("tag name", "li")

            while True:
                li = random.choice(format_li)  # 随机选择一个元素

                li.click()

                if "selected" in li.get_attribute("class"):
                    break

    driver.find_elements("css selector", '[data-type="cart"]')[-1].click()


# 3、对新增的用户进行个人信息的修改（仅修改性别和昵称）

def update_user(driver, nickname):
    driver.find_element("xpath", "//span[text()='个人中心']").click()
    driver.find_element("css selector", ".am-icon-edit").click()
    driver.find_element("partial link text", "编辑").click()
    driver.find_element("name", "nickname").send_keys(nickname)
    random.choice(driver.find_elements("class name", "am-icon-checked")).click()
    driver.find_elements("css selector", ".am-btn-primary")[-1].click()


if __name__ == '__main__':
    driver_ = webdriver.Chrome()
    driver_.implicitly_wait(10)
    driver_.maximize_window()
    driver_.get("http://shop-xo.hctestedu.com/")
    user_name = pass_word = f"test_{str(time.time()).replace('.', '')[5::]}"

    registered(driver_, user_name, user_name)
    add_goods_to_cart(driver_)
    update_user(driver_, "这是一个封装好的昵称")
