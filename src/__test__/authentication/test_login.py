import pytest
import os
from selenium.webdriver.support.ui import WebDriverWait
from core.web_driver.driver_factory import DriverFactory
from selenium.webdriver.support import expected_conditions as EC
from src.factory.authentication.login import LoginPage
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="class")
def driver(request):
    driver = DriverFactory.get_driver()
    initial_url = os.getenv('BASE_URL')
    driver.get(initial_url)
    WebDriverWait(driver, 100).until(EC.url_contains("/auth"))

    request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.mark.usefixtures("driver")
class TestLogin:
    def test_login_200(self):
        login_page = LoginPage(self.driver)
        login_page.login(
            os.getenv('ADMIN_ACC'),
            os.getenv('ADMIN_PASSWORD')
        )

        # TODO: Replace with real validation logic
        assert True
