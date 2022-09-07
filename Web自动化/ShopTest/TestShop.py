import time
import unittest

from selenium.webdriver.common.by import By

from ShopTest.common.ShopXo import ShopXo


class TestShop(unittest.TestCase):

    def test_login(self):
        """
        正向用例：
            正确的账号，正确的密码
        :return:
        """
        shopXo = ShopXo()
        shopXo.login("15652825886", "123456")
        time.sleep(10)

        user_info_ele = shopXo.driver.find_element(By.XPATH, "//div[@class='menu-hd']//em[2]")

        assert "15652825886" in user_info_ele.text





