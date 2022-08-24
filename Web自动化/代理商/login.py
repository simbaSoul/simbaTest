import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://localhost:8080/login.action")

usercode = driver.find_element("css selector", 'input[id="usercode"]')
time.sleep(1)
usercode.send_keys("admin")

password = driver.find_element("css selector", 'input[id="userpassword"]')
time.sleep(1)
password.send_keys("123456")

login_btn = driver.find_element(By.XPATH, "/html/body/div[2]/form/input")
time.sleep(1)
login_btn.click()

xtgl = driver.find_element(By.LINK_TEXT, "系统管理")
driver.implicitly_wait(3)  # 隐性等待 只要使用一次 单位为秒
xtgl.click()

jsgl = driver.find_element(By.LINK_TEXT, "角色管理")
time.sleep(1)
jsgl.click()

add_js = driver.find_element("id", "addRole")
time.sleep(1)
add_js.click()

input_js = driver.find_element("id", "a_roleName")
time.sleep(1)
input_js.send_keys("员工")

save_btn = driver.find_element("id", "addRoleSubmit")
time.sleep(2)
save_btn.click()
