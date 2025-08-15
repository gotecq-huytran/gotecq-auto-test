from typing import Tuple
from selenium.webdriver.remote.webdriver  import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from time import sleep
from model.const import DEFAULT_TIME_OUT 
import logging

Locator = Tuple[str, str] #attr and key
class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = DEFAULT_TIME_OUT):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=timeout)
    
    def open(self, url: str) -> None:
        self.driver.get(url)
        self.driver.implicitly_wait(5)

    def get_cookies(self):
        return self.driver.get_cookies()
    
    def get_cookie(self, name: str):
        return self.driver.get_cookie(name)
    
    def wait_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))
    
    def find(self, locator: Locator) -> WebElement:
        by, value = locator
        element = self.wait.until(EC.visibility_of_element_located(locator))
        if element:
            logging.info(f"🔍 Find element: {by}={value}")
        else:
            logging.warning(f"❌ Find 0 elements through: {by}={value}")
        return element

    def click(self, locator: Locator) -> None:
        element = self.wait.until(EC.element_to_be_clickable(locator)) 
        element.click()
        sleep(1)
    
    def keyAction(self, locator: Locator, keys: Keys):
        element = self.find(locator)
        element.send_keys(keys)
       
    def type(self, locator: Locator, text: str) -> None:
       element = self.find(locator)
       element.send_keys(text)
       logging.info(f"✅ send_keys('{text}').")

    def set_dropdown(self, locator, value: str = None, test_id: str = None, op_locator: Locator = None):
        self.click(locator)
        opt_wait = WebDriverWait(self.driver, timeout=5)
        option_locators = []

        if op_locator:
            option_locators.append(op_locator)
        else:
            option_locators.extend(
                [
                    (
                        By.CSS_SELECTOR,
                        f'[data-element-key="{test_id}-dropdown"] > .rc-virtual-list [label="{value}"]',
                    ),
                    (
                        By.CSS_SELECTOR,
                        f'[data-element-key="{test_id}-dropdown"] > li[data-menu-id*="{value}"]',
                    ),
                ]
            )
        for ol in option_locators:
            try:
                opt = opt_wait.until(EC.element_to_be_clickable(ol))
                opt.click()
                return opt
            except TimeoutException:
                continue

        raise TimeoutException(f"Dropdown option '{value}' not found for {locator}")

   

