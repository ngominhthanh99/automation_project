from selenium.webdriver.common.by import By
from base.base_page import BasePage

class LoginPage(BasePage):
    username_input = (By.XPATH, "//input[@placeholder='Username']")
    password_input = (By.XPATH, "//input[@placeholder='Password']")
    login_button = (By.XPATH, "//input[@id='login-button']")

    def login(self, username, password):
        self.send_keys(self.username_input, username)
        self.send_keys(self.password_input, password)
        self.click(self.login_button)
