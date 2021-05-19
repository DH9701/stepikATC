from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

#проверяем значение атрибута checked у people_radio
    num1 = browser.find_element_by_id ("num1")
    num2 = browser.find_element_by_id ("num2")
    x = int(num1.text)
    y = int(num2.text)
    z = str(x + y)
    drop = Select(browser.find_element_by_id ("dropdown"))
    drop.select_by_visible_text(z)
    browser.find_element_by_tag_name("button").click()
    
    time.sleep(10)
    
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
