import time
import unittest
from ShopTest.common.ShopXo import ShopXo


class TestShop(unittest.TestCase):

    def test_login(self):
        shopXo = ShopXo()
        shopXo.login("15652825886", "123456")
        time.sleep(10)
        shopXo.driver.get("https://www.baidu.com")
