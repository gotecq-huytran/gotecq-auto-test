from selenium.webdriver.common.by import By

def xPathSelector(xpath: str) -> str:
    return (By.XPATH, xpath)

def cssSelector(selector: str):
    return (By.CSS_SELECTOR, selector)

def xPathByElementKey(key: str) -> str:
    pattern = f"//*[@data-element-key='{key}']"
    return (By.XPATH, pattern) 

def cssSelectorForDropdown(dropdownClassName: str, value: str):
    pattern = f'.{dropdownClassName} div[title="{value}"]'
    return (By.CSS_SELECTOR, pattern)

