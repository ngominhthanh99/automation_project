import pytest
from selenium import webdriver
from utils.config_reader import ConfigReader
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="class")
def setup(request):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--remote-debugging-port=9222")

    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(ConfigReader.get_base_url())
    
    request.cls.driver = driver
    request.cls.config = ConfigReader.load_config()
    yield
    driver.quit()
