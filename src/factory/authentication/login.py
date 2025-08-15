from selenium.webdriver.common.by import By

from src.core.base_page import BasePage
from src.utils.selector import xPathByElementKey


class LoginPage(BasePage):
    username_el = (By.XPATH, xPathByElementKey("kc.login.form.input.email"))
    password_el = (By.XPATH, xPathByElementKey("kc.login.form.input.password"))
    login_button_el = (By.XPATH, xPathByElementKey("kc.login.form.button.login"))

    def login(self, username, password):
        self.type(self.username_el, username)
        self.type(self.password_el, password)
        self.click(self.login_button_el)
