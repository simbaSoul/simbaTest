from selenium import webdriver

# 标签之间的切换：

# 记住标签是对象，标签的切换使用的是标签对象的名称
driver = webdriver.Chrome()
driver.get("http://shop-xo.hctestedu.com/")
driver.switch_to.new_window("tap")  # 无论是窗口 还是标签， 都是获取对象名
driver.get("https://www.baidu.com")

# 获取标签页的名称
# driver.window_handles 标签对象名称的列表


driver.switch_to.window(driver.window_handles[0])  # 切换标签的方式，接受标签名（句柄） 标签对象的名称
print(driver.title)
driver.switch_to.window(driver.window_handles[1])
print(driver.title)

# 作业 在新标签打开所有商品链接 判断是否于商品一致
