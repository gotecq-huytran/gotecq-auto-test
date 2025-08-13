import os

import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from core.web_driver.driver_factory import DriverFactory
from src.model.const import DEFAULT_WAIT_TIME_OUT

initial_url = os.getenv("BASE_URL")


@pytest.fixture(scope="class")
def driver(request):
    driver = DriverFactory.get_driver()
    initial_url = os.getenv("BASE_URL")
    driver.get(initial_url)
    # wait to redirect back home
    WebDriverWait(driver, timeout=DEFAULT_WAIT_TIME_OUT).until(EC.url_contains("/auth"))

    request.cls.driver = driver
    yield driver

    driver.quit()
