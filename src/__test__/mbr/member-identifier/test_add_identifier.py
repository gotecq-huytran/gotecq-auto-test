from src.__test__.authentication.login import TestLogin
from src.factory.home_page.app_access import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from utils.selector import xPathByElementKey
from utils.datetime import dateGeneration
from datetime import date, timedelta
import logging
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
        identifierMenu =  xPathByElementKey(
            'mbr.member-menu.identifier'
        )
        page.click(identifierMenu)

        return page

    def test_add_member_identifier(self):
        logging.info('Open add identifier form')
        today = date.today()
        yesterday = today - timedelta(days=1)

        page = self.__access_member_identifier()
        #open adding form
        page.click(xPathByElementKey('mbr.add-identifier-button'))

        #select each field
        page.set_dropdown(
            xPathByElementKey('mbr.form.identifier.type__coding'),
            'Taxpayer Identification Number (TIN)',
            'mbr.form.identifier.type__coding' 
        )
        page.type(
            xPathByElementKey('mbr.form.identifier.value'),
            text=10
        )
        page.set_dropdown(
            xPathByElementKey('mbr.form.identifier.use'),
            'Primary',
            'mbr.form.identifier.use' 
        )
        page.type(
            xPathByElementKey('mbr.form.identifier.assigner'),
            text='tester'
        )
        page.type(
            xPathByElementKey('mbr.form.identifier.period__start'),
            text=dateGeneration(yesterday)
        )
        page.type(
            xPathByElementKey('mbr.form.identifier.period__end'),
            text=dateGeneration()
        )
        page.wait_invisible(xPathByElementKey('mbr.form.create-identifier'))


       