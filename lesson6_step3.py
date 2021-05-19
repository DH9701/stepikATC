from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest
import time
import math

final = ''


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()
    print(final)


@pytest.mark.parametrize('number', [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905])
def test(browser, number):
    global final
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)
    answer = str(math.log(int(time.time())))
    text_area = browser.find_element_by_tag_name("textarea")
    text_area.send_keys(answer)
    button = browser.find_element_by_class_name("submit-submission")
    button.click()
    message = browser.find_element_by_class_name("smart-hints__hint")
    try:
        assert "Correct" in message.text
    except AssertionError:
        final += message.text  # собираем ответ про Сов с каждой ошибкой
