from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class ShopXo:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://shop-xo.hctestedu.com/")
    Wait = Wait(driver, 5)

    def login(self, user_name, pass_word):
        # 定位登录按钮
        home_page_login_locator = (By.XPATH, '//div[@class="menu-hd"]/a[text()="登录"]')
        home_page_login_ele = self.Wait.until(EC.visibility_of_element_located(home_page_login_locator))
        home_page_login_ele.click()  # 点击登录按钮

        # 定位帐号输入框
        user_name_locator = (By.XPATH, '//div[@class="am-tabs-bd"]//input[@name="accounts"]')
        user_name_ele = self.Wait.until(EC.visibility_of_element_located(user_name_locator))
        user_name_ele.send_keys(user_name)

        # 定位密码输入框
        pwd_locator = (By.XPATH, '//div[@class="am-input-group am-input-group-sm"]//input[@name="pwd"]')
        pwd_ele = self.Wait.until(EC.visibility_of_element_located(pwd_locator))
        pwd_ele.send_keys(pass_word)

        # 定位登录按钮
        login_locator = (
            By.XPATH, '//div[@class="am-form-group am-form-group-refreshing am-margin-top-lg"]//button[@type="submit"]')
        login_ele = self.Wait.until(EC.visibility_of_element_located(login_locator))
        login_ele.click()


if __name__ == '__main__':
    ShopXo().login("15652825886", "123456")
