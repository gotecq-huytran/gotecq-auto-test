from core.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urljoin
from src.model.const import DEFAULT_TIME_OUT
from src.__test__.conftest import initial_url
import os

class HomePage(BasePage):
    initial_url = os.getenv('BASE_URL')

    def accessApp(self, app: str):
        app_url = urljoin(self.initial_url,f'/tecq/{app}')
        selector = f'a[href*="{app_url}"]'
        APP_PORTAL = (By.CSS_SELECTOR, selector)
        wait = WebDriverWait(self.driver, timeout=DEFAULT_TIME_OUT)
        element = wait.until(EC.visibility_of_element_located(APP_PORTAL))
        # Dùng js để trigger click thay vì element.click() của selenium
        # để fix lỗi element click intercepted
        self.driver.execute_script("arguments[0].click();", element)
