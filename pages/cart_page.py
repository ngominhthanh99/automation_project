from selenium.webdriver.common.by import By
from base.base_page import BasePage

class CartPage(BasePage):
    checkout_btn = (By.XPATH, "//button[@id='checkout']")

    def click_checkout(self):
        self.wait_for_element(self.checkout_btn)
        self.click(self.checkout_btn)
