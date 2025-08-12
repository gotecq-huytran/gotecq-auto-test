from core.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.__test__.conftest import initial_url
from src.model.const import DEFAULT_TIME_OUT
import os

class HomePage(BasePage):
    initial_url = os.getenv('BASE_URL')

    def accessApp(self, app: str):
        app_url = self.initial_url + '/tecq/' + app
        selector = f'a[href*="{app_url}"]'
        APP_PORTAL = (By.CSS_SELECTOR, selector)
        wait = WebDriverWait(self.driver, timeout=DEFAULT_TIME_OUT)
        wait.until(EC.visibility_of_element_located(APP_PORTAL))
        self.click(APP_PORTAL)
       
