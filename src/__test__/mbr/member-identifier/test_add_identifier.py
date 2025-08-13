
from src.__test__.authentication.login import TestLogin
from src.factory.home_page.app_access import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from utils.selector import xPathByElementKey
from model.const import DEFAULT_TIME_OUT
import logging
import pytest
load_dotenv()

class TestAddMemberIdentifier(TestLogin):
    def __access_module(self):
        driver = self.driver
        self.login()
        homePage = HomePage(driver)
        homePage.accessApp('mbr')

        return homePage
    
    def __access_member_identifier(self):
        logging.info("Access mbr app and identifier panel")
        page = self.__access_module()
        identifierMenu = (By.XPATH, xPathByElementKey(
            'mbr.member-menu.identifier'
        ))
        page.click(identifierMenu)

        return page
    
    # def __clickInputByXpath(self, xpath: str, page):
    #     page.click((By.XPATH, xpath))


    def test_add_member_identifier(self):
        logging.info('Open add identifier form')
        page = self.__access_member_identifier()
        #open adding form
        
        # self.__clickInputByXpath("//label[.//p[text()='Identifier']]//following::input", page)
        



