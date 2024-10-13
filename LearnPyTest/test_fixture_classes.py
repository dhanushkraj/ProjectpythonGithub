from time import sleep
from selenium import webdriver
import pytest


@pytest.fixture(scope="class")
def init_chrome_driver(request):
    ch_driver = webdriver.Chrome()
    request.cls.driver = ch_driver
    yield
    ch_driver.close()


@pytest.fixture(scope="class")
def init_edge_driver(request):
    ed_driver = webdriver.Edge()
    request.cls.driver = ed_driver
    yield
    ed_driver.close()


@pytest.mark.usefixtures("init_chrome_driver")
class Base_Chrome_Test:
    pass


class Test_Google_Chrome(Base_Chrome_Test):

    def test_google_title_chrome(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == "Google"


@pytest.mark.usefixtures("init_edge_driver")
class Base_ed_Test:
    pass


class Test_ed_Chrome(Base_Chrome_Test):

    def test_ed_title_chrome(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == "Google"

