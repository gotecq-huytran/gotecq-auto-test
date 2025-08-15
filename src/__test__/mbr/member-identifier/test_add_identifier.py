from src.__test__.authentication.login import TestLogin
from src.factory.home_page.app_access import HomePage
from src.core.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from utils.selector import xPathByElementKey, cssSelectorForDropdown, xPathSelector, cssSelector
from utils.datetime import dateGeneration
from datetime import date, timedelta
import logging
from time import sleep
load_dotenv()
class TestAddMemberIdentifier(TestLogin):
    ADD_BUTTON_LOCATOR = xPathByElementKey('mbr.add-identifier-button')
    ADD_FORM_LOCATOR =  xPathByElementKey('mbr.form.create-identifier')
    EDIT_FROM_LOCATOR = xPathByElementKey('mbr.form.edit-identifier')
    TYPE_CODING_FIELD =  'mbr.form.identifier.type__coding'
    VALUE_FIELD = 'mbr.form.identifier.value'
    ASSIGNER_FIELD = 'mbr.form.identifier.assigner'
    PERIOD_START_FIELD = '#mbr-form-identifier-period__start'
    PERIOD_END_FIELD = '#mbr-form-identifier-period__end'
    DELETE_BUTTON_LOCATOR = xPathSelector("//div[contains(@class, 'identifier-delete-overlay')]//button//span[text()='Delete']")

    assignor = 'tester--' + dateGeneration()
    page: BasePage
    periodStart = date.today()
    periodEnd  = periodStart + timedelta(days=1)
    

    def __access_module(self):
        driver = self.driver
        self.login()
        homePage = HomePage(driver)
        homePage.accessApp('mbr')
        self.page = homePage

        return homePage
    
    def __access_member_identifier(self):
        logging.info("Access mbr app and identifier panel")
        page = self.__access_module()
        identifierMenu =  xPathByElementKey(
            'mbr.member-menu.identifier'
        )
        page.click(identifierMenu)

        return page

    def __findActionButtonOnAddedRow(self, className: str):
        pattern = f"//div[contains(@class, 'table-cell')][./div[text()='{self.assignor}']]/following::button[contains(@class, '{className}')][1]"
        return (By.XPATH, pattern)

    def add_member_identifier(self):
        logging.info('Open add identifier form')
       

        page = self.__access_member_identifier()
        #open adding form
        page.click(self.ADD_BUTTON_LOCATOR)
        #select each field
        page.set_dropdown(
            xPathByElementKey(self.TYPE_CODING_FIELD),
            'Taxpayer Identification Number (TIN)',
            self.TYPE_CODING_FIELD 
        )
        page.type(
            xPathByElementKey(self.VALUE_FIELD),
            text=10
        )
        page.set_dropdown(
            locator=xPathSelector("//p[text()='Identifier Use']//following::input[1]"),
            op_locator=cssSelectorForDropdown(
                dropdownClassName='mbr-form-identifier-use-dropdown',
                value='Official'
            )
        )
        page.type(
            xPathByElementKey(self.ASSIGNER_FIELD),
            text=self.assignor
        )
        page.type(
            cssSelector(self.PERIOD_START_FIELD),
            text=dateGeneration(self.periodStart)
        )
        page.type(
            cssSelector(self.PERIOD_END_FIELD),
            text=dateGeneration(self.periodEnd)
        )

        #this Tab action will remove the focus on the field
        page.keyAction(cssSelector(self.PERIOD_END_FIELD), Keys.ENTER)
        #submit the form
        page.click(
            cssSelector('[data-element-key="mbr.form.create-identifier"] button[type="submit"]')
        )
        
        page.wait_invisible(self.ADD_FORM_LOCATOR)


    def edit_member_identifier(self):
        sleep(2)
        addButton = self.__findActionButtonOnAddedRow('actionbtn-edit')
        page = self.page
        #open edit form
        page.click(addButton)
        #edit period start and period end
        page.type(
            cssSelector(self.PERIOD_START_FIELD),
            text=dateGeneration(self.periodStart + timedelta(days=10))
        )
        page.type(
            cssSelector(self.PERIOD_END_FIELD),
            text=dateGeneration(self.periodEnd + timedelta(days=10))
        )

        #this Tab action will remove the focus on the field
        page.keyAction(cssSelector(self.PERIOD_END_FIELD), Keys.ENTER)
        #submit the form
        page.click(
            cssSelector(f'[data-element-key="mbr.form.edit-identifier"] button[type="submit"]')
        )

        page.wait_invisible(self.EDIT_FROM_LOCATOR)


    def delete_member_identifier(self):
        sleep(2)
        page = self.page
        deleteAction = self.__findActionButtonOnAddedRow('actionbtn-delete')
        page.click(deleteAction)
        page.click(self.DELETE_BUTTON_LOCATOR)
        sleep(1)
        page.wait_invisible(self.DELETE_BUTTON_LOCATOR)

    def test(self):
        self.add_member_identifier()
        self.edit_member_identifier()
        self.delete_member_identifier()


        


