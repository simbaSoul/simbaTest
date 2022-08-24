import time
import unittest
import requests


class MyTestCase(unittest.TestCase):
    baseUrl = "http://192.168.200.110/"
    timestamp = int(round(time.time() * 1000))

    def test_get_code(self):
        """
        获取验证码
        :return:
        """
        data = {
            "phone": "15652825886",
            "codeType": 0
        }
        headers = {
            "timestamp": str(self.timestamp),
            "source-type": "1"
        }
        yqjg = {
            "code": "0","msg": "成功"
        }
        r = requests.get(self.baseUrl + "/api/sms/verifyCode", data=data, headers=headers)
        data = {
            "phone": "15652825886",
            "sms": "0000"
        }
        r = requests.post(self.baseUrl + "/api/user/login/sms", data=data, headers = headers)
        self.assertEqual(r.status_code, 200,msg="接口请求失败")
        self.assertEqual("成功",r.json()["msg"],msg="登录失败")
        self.assertIsNotNone(r.json()["data"],msg="没有返回token")

        print(r.json())


    def test_get_classifyTree(self):
        headers = {
            "timestamp": str(self.timestamp),
            "source-type": "1"
        }
        r = requests.get(self.baseUrl + "/api/home/classifyTree", headers=headers)
        self.assertEqual(r.json()["msg"],"成功",msg="接口访问失败")
        self.assertIsNotNone(r.json()["data"])
        print(r.json()["data"])

if __name__ == '__main__':
    unittest.main()
