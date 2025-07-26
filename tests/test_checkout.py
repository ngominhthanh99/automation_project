import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from base.base_test import setup

@allure.suite("Checkout Tests")
@allure.title("Test Checkout Success")
@allure.description("Ensure user can complete checkout process")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.usefixtures("setup")
class TestCheckout:
    def test_checkout(self):
        inventory = InventoryPage(self.driver)
        cart = CartPage(self.driver)
        checkout = CheckoutPage(self.driver)
        inventory.add_products(3)
        inventory.click_cart()
        cart.click_checkout()
        checkout.information("John", "Doe", "70000")
        checkout.click_continue_btn()
        checkout.click_finish_btn()

        message = checkout.confirmation_text()
        assert "Your order has been dispatched, and will arrive just as fast as the pony can get there!" in message
