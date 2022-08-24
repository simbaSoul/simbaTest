import unittest

from Api自动化 import register


class MyTestCase(unittest.TestCase):
    def test_register_success(self):
        username = "qwerty"
        pwd = "123456"
        pwd1 = "123456"

        yqjg = {
            "code" : 1,
            "msg" : "注册成功！"
        }
        r = register.register(username, pwd, pwd1)
        self.assertEqual(yqjg,r)


if __name__ == '__main__':
    unittest.main()
