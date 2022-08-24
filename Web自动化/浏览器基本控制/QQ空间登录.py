# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("https://qzone.qq.com/")
#
# time.sleep(2)
#
# # driver.find_element(by=By.XPATH,value='//*[@id="switcher_plogin"]').click()
# driver.find_element(by=By.ID,value=("u")).send_keys("849519881")
#
# # driver.close()

# def a(*args):
#
#     result = 0
#
#     for i in range(len(args)):
#         if i == len(args)-1:
#             return result
#         else:
#             result += args[i] // args[i+1]
#
#     return result
#
# print(a(100,24,22,36))


def b(s):
    flag = False
    if " " in s:
        flag = True
        return flag
    else:
        return flag



print(b("hell oworld"))