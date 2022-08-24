import time

from selenium import webdriver  # 导入selenium，会将selenium相关的操作方式加载到你的内存

# 打开浏览器--->构建一个selenium的webdriver的浏览器实例
driver = webdriver.Chrome()  # 打开的是chrome浏览器
#webdriver.Firefox() # 打开的是火狐浏览器
#webdriver.Ie()  #打开的是Ie浏览器
# 输入网址
#固定写法：
driver.get("http://bbs.hctestedu.com/")
time.sleep(10)
#退出浏览器  # 固定写法
driver.quit()
