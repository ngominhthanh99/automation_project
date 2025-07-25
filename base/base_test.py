import pytest
from selenium import webdriver
from utils.config_reader import ConfigReader

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(ConfigReader.get_base_url())
    request.cls.driver = driver
    request.cls.config = ConfigReader.load_config()
    yield
    driver.quit()
