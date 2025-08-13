from core.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.__test__.conftest import initial_url
import os

class HomePage(BasePage):
    initial_url = os.getenv('BASE_URL')

    def accessApp(self, app: str):
        app_url = self.initial_url + '/tecq/' + app
        selector = f'a[href*="{app_url}"]'
        portalElement = (By.CSS_SELECTOR, selector)
        self.click(portalElement)
       
