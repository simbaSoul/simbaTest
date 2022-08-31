import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait



driver = webdriver.Chrome()

driver.get("D:\\tender_dj\PycharmProjects\Web自动化\华测商城\Frame_html\index.html")

frame1 = driver.find_element(By.ID, "frame1")
driver.switch_to.frame(frame1)
h4 = driver.find_element(By.XPATH, "/html/body/h4")
print(h4.text)


frame2 = driver.find_element(By.NAME, "frame2")
driver.switch_to.frame(frame2)

alter = driver.find_element(By.XPATH, '//*[@id="alert"]')
alter.click()
a = driver.switch_to.alert.text
print(a)

driver.switch_to.alert.accept()

btn = driver.find_element(By.ID, "confirm")
btn.click()

print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()

frame3 = driver.find_element(By.NAME, "frame3")
driver.switch_to.frame(frame3)
i4 = driver.find_element(By.XPATH, '//iframe[@src="frame4.html"]')
driver.switch_to.frame(i4)

p = driver.find_element(By.XPATH, "/html/body/div/div[1]/p")
print(p.text)

wu = driver.find_element(By.ID, "open_win")
wu.click()

frame7 = driver.find_element(By.ID, "frame7")
driver.switch_to.frame(frame7)

qi = driver.find_element(By.XPATH, "/html/body/p").text
print(qi)
driver.switch_to.parent_frame()

close = driver.find_element(By.ID, "close_win")
close.click()

