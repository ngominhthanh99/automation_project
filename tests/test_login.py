import pytest
from pages.login_page import LoginPage
from base.base_test import BaseTest
from utils.config_reader import ConfigReader
import allure


@allure.suite("Login Tests")
@allure.title("Test Login Success")
@allure.description("Thanh test Login")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures("setup")

class TestLogin(BaseTest):
    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.login(ConfigReader.get_username(), ConfigReader.get_password())
  