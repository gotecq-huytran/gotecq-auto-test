import os
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from src.core.web_driver.driver_factory import DriverFactory
from src.model.const import DEFAULT_TIME_OUT
from dotenv import load_dotenv

load_dotenv()
initial_url = os.getenv("BASE_URL")

@pytest.fixture(scope="class")
def driver(request):
    driver = DriverFactory.get_driver()
    driver.get(initial_url)
    # wait to redirect back home
    WebDriverWait(driver, timeout=DEFAULT_TIME_OUT).until(EC.url_contains("/auth"))

    request.cls.driver = driver
    yield driver

    driver.quit()
