from selenium import webdriver

driver1 = webdriver.Chrome()
driver2 = webdriver.Chrome()
driver3 = webdriver.Chrome()
driver1.get("http://www.baidu.com")
driver2.close() # 线程不会销毁
driver3.quit()  # 线程销毁，内存回收
