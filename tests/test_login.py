import pytest
from pages.login_page import LoginPage
from base.base_test import setup

@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_successful_login(self):
        login_page = LoginPage(self.driver)
        login_page.login(self.config["username"], self.config["password"])


