from selenium.webdriver.common.by import By

def xPathSelector(xpath: str) -> str:
    return (By.XPATH, xpath)

def xPathByElementKey(key: str) -> str:
    pattern = f"//*[@data-element-key='{key}']"
    return (By.XPATH, pattern) 

