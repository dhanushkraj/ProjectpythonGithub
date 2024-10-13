from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    ...


class TestHubSpot(BaseTest):

    @pytest.mark.parametrize("username, password", [("admin@gmail.com","admin132"),
                                                    ("naveen@gmail.com", "naveen123")])
    def test_login(self, username, password):
        """
        This is method is used to login into hubspot
        :param username:
        :param password:
        :return:
        """
        self.driver.get("https://app.hubspot.com/login")
        self.driver.maximize_window()
        self.driver.find_element("id", "username").send_keys(username)
        self.driver.find_element("id", "password").send_keys(password)
        sleep(3)


















