from typing import Tuple

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.model.const import DEFAULT_WAIT_TIME_OUT

Locator = Tuple[str, str]  # attr and key


class BasePage:
    def __init__(self, driver: WebDriver, timeout=DEFAULT_WAIT_TIME_OUT):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=timeout)

    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def open(self, url: str):
        self.driver.get(url)

    def find(self, locator: Locator):
        return self.driver.find_element(*locator)

    def finds(self, locator: Locator):
        return self.driver.find_elements(*locator)

    def click(self, locator: Locator):
        el = self.wait.until(EC.element_to_be_clickable(locator))
        el.click()
        return el

    def type(self, locator: Locator, text: str):
        self.find(locator).send_keys(text)

    def set_text(self, locator, text: str):
        el = self.wait_visible(locator)
        el.send_keys(text)
        return el

    def set_dropdown(self, locator, value: str, test_id: str, op_locator: Locator):
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
