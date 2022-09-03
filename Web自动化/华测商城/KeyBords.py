import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

# options = webdriver.ChromeOptions()
# # options.headless = True
# options.page_load_strategy = "none"
driver = webdriver.Chrome()

driver.get("http://shop-xo.hctestedu.com/")
# located = (By.ID, "search-input")
# ele = Wait(driver, 10).until(EC.visibility_of_element_located(located))
# ele.send_keys("手机", Keys.CONTROL + "A")

# 左键点击
# search_locator = driver.find_element(By.ID, "ai-topsearch")
action = ActionChains(driver)

located = (By.ID, "search-input")
login_located = (By.LINK_TEXT, "登录")
input_ele = Wait(driver, 3).until(EC.visibility_of_element_located(located))
login_ele = Wait(driver, 3).until(EC.visibility_of_element_located(login_located))
action.drag_and_drop(login_ele, input_ele)
action.perform()






