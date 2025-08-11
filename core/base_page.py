from typing import Tuple
from selenium.webdriver.remote.webdriver  import WebDriver
from selenium.webdriver.remote.webelement import WebElement

Locator = Tuple[str, str] #attr and key
class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    def open(self, url: str) -> None:
        self.driver.get(url)

    def find(self, locator: Locator) -> WebElement:
        return self.driver.find_element(*locator)

    def finds(self, locator: Locator) -> WebElement:
        return self.driver.find_elements(*locator)

    def click(self, locator: Locator) -> None:
        self.find(locator).click()

    def type(self, locator: Locator, text: str) -> None:
       self.find(locator).send_keys(text)