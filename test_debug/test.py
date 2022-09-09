from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://zhushuju.test.jk.com/login')
# driver.find_element('xpath', '//input[@type="text"]')
# driver.find_element('xpath', '//input[@type="password"]')
driver.find_element('xpath', '//span[text()="登 录"]').click()

time.sleep(5)
# text = driver.find_elements(By.CSS_SELECTOR, ".el-form-item__error")
text = driver.find_element('css selector', ".el-form-item__error")
print(text.text)
# print(text[1].text)

driver.close()
