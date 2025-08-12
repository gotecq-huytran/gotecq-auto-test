
from src.__test__.authentication.login import TestLogin
from src.factory.home_page.app_access import HomePage
from dotenv import load_dotenv
load_dotenv()

class TestAddMemberIdentifier(TestLogin):
    def test_access_module(self):
        driver = self.driver
        self.login()
        homePage = HomePage(driver)
        homePage.accessApp('mbr')
        assert True
