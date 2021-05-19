from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    browser.find_element_by_tag_name("button").click()
    
    alert = browser.switch_to.alert
    alert.accept()

    x = int(browser.find_element_by_id ("input_value").text)
    z = calc(x)
    input1 = browser.find_element_by_id ("answer")
    input1.send_keys(z)
    
    
    
    browser.find_element_by_tag_name("button").click()
    
    time.sleep(10)
    
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
