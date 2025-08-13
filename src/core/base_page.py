from typing import Tuple
from selenium.webdriver.remote.webdriver  import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import logging
from model.const import DEFAULT_TIME_OUT 
Locator = Tuple[str, str] #attr and key
class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = DEFAULT_TIME_OUT):
        self.driver = driver
        self.timeout = timeout
    
    def open(self, url: str) -> None:
        self.driver.get(url)
        self.driver.implicitly_wait(5)

    def get_cookies(self):
        return self.driver.get_cookies()
    
    def get_cookie(self, name: str):
        return self.driver.get_cookie(name)
    
    def find(self, locator: Locator) -> WebElement:
        by, value = locator
        wait = WebDriverWait(self.driver, timeout=self.timeout)
        wait.until(EC.visibility_of_element_located(locator))
        element = self.driver.find_element(*locator)
        if element:
            logging.info(f"🔍 Find element: {by}={value}")
        else:
            logging.warning(f"❌ Find 0 elements through: {by}={value}")
        return element

    def click(self, locator: Locator) -> None:
        element = self.find(locator)
        element.click()

    def type(self, locator: Locator, text: str) -> None:
       element = self.find(locator)
       element.clear()
       element.send_keys(text)
       logging.info(f"✅ send_keys('{text}').")

    
   

