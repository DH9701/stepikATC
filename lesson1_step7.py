from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

#проверяем значение атрибута checked у people_radio
    img = browser.find_element_by_tag_name("img")
    x = img.get_attribute("valuex")
    val = calc(x)
    
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(str(val))
    
    option1 = browser.find_element_by_css_selector("[type='checkbox']")
    option1.click()
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(10)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
