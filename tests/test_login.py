import pytest
from pages.login_page import LoginPage
# from base.base_test import setup
from base.base_test import BaseTest
import allure


@allure.suite("Login Tests")
@allure.title("Test Login Success")
@allure.description("Verify user can login with valid credentials")
@allure.severity(allure.severity_level.CRITICAL)

# @pytest.mark.usefixtures("setup")
class TestLogin(BaseTest):
    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.login(self.config["username"], self.config["password"])