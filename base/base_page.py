from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config_reader import ConfigReader

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def wait_for_element(self, locator):
        timeout = ConfigReader.get_timeout()
        return WebDriverWait(self.driver).until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.wait_for_element(locator).click()

    def send_keys(self, locator, text):
        self.wait_for_element(locator).send_keys(text)
        
    def get_text(self, locator):
        return self.wait_for_element(locator).text    
