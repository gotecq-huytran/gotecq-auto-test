from selenium.webdriver.remote.webdriver import WebDriver
from src.factory.authentication.login import LoginPage
import pytest
import os
from dotenv import load_dotenv

load_dotenv()
@pytest.mark.usefixtures("driver")
class TestLogin():
    driver: WebDriver
    def login(self):
        loginPage = LoginPage(self.driver)
        loginPage.login(
            os.getenv('ADMIN_ACC'),
            os.getenv('ADMIN_PASSWORD')
        )

    def login_200(self):
        self.login()
        # TODO: Replace with real validation logic
        assert True
  