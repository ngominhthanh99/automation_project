from selenium.webdriver.common.by import By
from base.base_page import BasePage

class CheckoutPage(BasePage):
    first_name = (By.XPATH, "//input[@placeholder='First Name']")
    last_name = (By.XPATH, "//input[@placeholder='Last Name']")
    postal_code = (By.XPATH, "//input[@placeholder='Zip/Postal Code']")
    continue_btn = (By.XPATH, "//input[@id='continue']")
    finish_btn = (By.XPATH, "//button[@id='finish']")
    confirmation = (By.XPATH, "//div[@class='complete-text']")

    def information(self, firstname, lastname):
        self.send_keys(self.first_name, firstname)
        self.send_keys(self.last_name, lastname)
        self.send_keys(self.postal_code)
        
    def click_continue_btn(self):
        self.click(self.continue_btn)

    def click_finish_btn(self):
        self.click(self.finish_btn)

    def confirmation_text(self):
        return self.wait_for_element(self.confirmation).text
