from selenium import webdriver

options = webdriver.ChromeOptions()  # 实例Chrome浏览器的配置项

# 开启无头模式 （无界面模式） 优点：减少浏览器的页面渲染；
# 无头模式是后台运行模式吗？不属于台运行模式；因为浏览器的渲染动作依然有，
# 仅仅不在你的计算机界面中显示了（代表着减少了你的显卡的工作量）
# options.headless = True

# driver = webdriver.Chrome(options=options)
# driver.get("http://shop-xo.hctestedu.com/")
# driver.save_screenshot("商城.png")

# 时间的设置
# driver = webdriver.Chrome()
#
# driver.set_page_load_timeout(3)  # 页面加载超时，一次性设置，所有资源的加载时间
# # 等待每个资源 --> 隐形等待
# driver.get("https://www.baidu.com")

# 全屏
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
# driver.fullscreen_window()
#
# # 设置浏览器的大小
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
# driver.set_window_size(100, 500)
# # 设置浏览器的位置
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
# driver.set_window_position(100, 500)
# # 同时设置浏览器的大小和位置
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
# driver.set_window_rect(100, 500, 200, 600)

# 新建标签或窗口

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.switch_to.new_window("tap")
driver.get("https://www.baidu.com")
driver.switch_to.new_window("window")
driver.get("http://shop-xo.hctestedu.com/")