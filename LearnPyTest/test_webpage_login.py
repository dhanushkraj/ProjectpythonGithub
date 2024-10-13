from time import sleep
import pytest
from selenium import webdriver


def test_google():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.google.co.in/")
    assert driver.title == "Google"
    sleep(5)
    driver.quit()


def test_facebook():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.facebook.com/")
    assert driver.title == "Facebook – log in or sign up"
    sleep(5)
    driver.quit()


def test_instagram():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.instagram.com/")
    assert driver.title == "Instagram"
    sleep(5)
    driver.quit()





















