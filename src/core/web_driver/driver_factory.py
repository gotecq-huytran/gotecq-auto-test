from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class DriverFactory:
    @staticmethod
    def get_driver(browser='chrome'):
        executablePath = './chromedriver'
        options = Options()
        options.add_argument('--start-maximized')
        if browser.lower() == 'chrome':
            return webdriver.Chrome(
                service=Service(ChromeDriverManager().install()),
                options=options
            )
        elif browser == 'safari':
            return webdriver.Safari()