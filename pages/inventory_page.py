from selenium.webdriver.common.by import By
from base.base_page import BasePage

class InventoryPage(BasePage):
    title = (By.XPATH, "//span[@class='title']")
    add_buttons = (By.XPATH, "//button[text()='Add to cart']")
    cart_icon = (By.XPATH, "//a[@class='shopping_cart_link']")

    def title_loaded(self):
        return self.wait_for_element(self.title).is_displayed()

    def add_products(self, count=3):
        buttons = self.driver.find_elements(*self.add_buttons)
        for btn in buttons[:count]:
            btn.click()

    def click_cart(self):
        self.click(self.cart_icon)