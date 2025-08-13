import os
from urllib.parse import urljoin

from selenium.webdriver.common.by import By

from core.base_page import BasePage


class HomePage(BasePage):
    initial_url = os.getenv("BASE_URL")

    def accessApp(self, app: str):
        app_url = urljoin(self.initial_url, f"tecq/{app}")
        APP_PORTAL = (By.CSS_SELECTOR, f'a[href*="{app_url}"]')

        ele = self.wait_visible(APP_PORTAL)
        # Dùng js để trigger click thay vì element.click() của selenium
        # để fix lỗi element click intercepted
        self.driver.execute_script("arguments[0].click();", ele)
