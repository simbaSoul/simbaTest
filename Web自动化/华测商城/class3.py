import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with, with_tag_name
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

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
    element = Wait(dr, time_out).until(EC.presence_of_element_located(cz))
    return element


def add_shop(goods, good_num):
    """

    :param goods: 商品属性列表
    :param good_num: 商品数量
    :return:
    """
    for i in goods:  # 遍历所有商品属性
        # 如果存在 sku-items，则说明商品属性有下级选项，否则说明没有下级选项
        if "sku-items" in i.get_attribute("class") and Wait(driver, 3).until(EC.visibility_of(i)):
            # 遍历下级选项
            while True:
                value = (By.CSS_SELECTOR, "ul>li")
                selected_located = (By.CSS_SELECTOR, ".theme-options>ul>li.selected")
                sku_items = i.find_elements(*value)  # 定位下级选项列表
                randint = random.randint(0, len(sku_items) - 1)
                sku_element = sku_items[randint]  # 随机生成一个下级元素
                if "sku-items-disabled" not in sku_element.get_attribute(
                        "class"):  # 如果sku-items-disabled属性不在下级元素属性里此元素说明可以点击
                    sku_element.click()
                    global theme_options
                    theme_options = Wait(driver, 3).until(
                        EC.visibility_of_all_elements_located(selected_located))  # 刷新页面已选择的元素
                    break
        else:
            i.find_element(By.TAG_NAME, "input").send_keys(good_num)
    driver.find_element(By.CSS_SELECTOR, ".cart-submit").click()
    return "添加成功"


# 获取注册按钮 并点击
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

# 获取首页商品链接
good_list = driver.find_element(By.CLASS_NAME, "goods-list")
good_hrefs = good_list.find_elements(By.TAG_NAME, "a")
for i in good_hrefs:
    i.get_attribute("href")
driver.get(good_hrefs[random.randint(0, len(good_hrefs) - 1)].get_attribute("href"))

# driver.get("http://shop-xo.hctestedu.com/index.php?s=/index/goods/index/id/9.html")
# 定位获取所有商品属性
theme_option = (By.CSS_SELECTOR, ".theme-options")
theme_options = Wait(driver, 3).until(EC.visibility_of_all_elements_located(theme_option))
add_shop(theme_options, 10)

cz = (By.XPATH, '//span[text()="个人中心"]')

grzx = user_register(driver, 2, cz)
grzx.click()
cz = (By.CLASS_NAME, "am-icon-edit")
xgzl = user_register(driver, 2, cz)
xgzl.click()

cz = (By.XPATH, '//a[text()=" 编辑"]')
bj = user_register(driver, 2, cz)
bj.click()

sr = (By.NAME, "birthday")
srl = user_register(driver, 2, sr)
srl.click()

fr = (By.XPATH, "/html/body/div[7]/iframe")
frs = driver.find_element(*fr) # 定位frame
driver.switch_to.frame(frs) # 切换到frame
driver.find_element(By.XPATH, "/html/body/div/div[3]/table/tbody/tr[3]/td[2]").click()
driver.switch_to.parent_frame() # 操作完要释放frame
