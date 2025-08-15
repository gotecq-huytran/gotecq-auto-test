from selenium import webdriver


class DriverFactory:
    @staticmethod
    def get_driver(browser="chrome"):
        match browser:
            case "chrome":
                driver = webdriver.Chrome()
            case "safari":
                driver = webdriver.Safari()

        driver.maximize_window()
        return driver
