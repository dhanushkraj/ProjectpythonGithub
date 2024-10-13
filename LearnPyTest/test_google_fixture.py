from time import sleep
from selenium import webdriver
import pytest


driver = None


@pytest.fixture(scope="module")
def init_driver():
    global driver
    print("-----------------setup------------------------")
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("http://www.google.com")
    yield
    print("-----------------teardown------------------------")
    driver.quit()


@pytest.mark.usefixtures("init_driver")
def test_google_title():
    assert driver.title == "Google"


def test_google_url(init_driver):
    assert driver.current_url == 'https://www.google.com/'

