from selenium.webdriver.common.by import By
from base.base_page import BasePage

class CartPage(BasePage):
    checkout_btn = (By.XPATH, "//button[text()='Checkout']")

    def click_checkout(self):
        self.click(self.checkout_btn)
