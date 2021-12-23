import pytest
from page import Page
from selenium import webdriver
from webdriver.firefox import GeckoDriverManager

@pytest.fixture(scope="session")
def browser():
    browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    browser.implicitly_wait(2)
    
    pytest.page = Page(browser, "https://www.work.ua/")
    
    try:
        yield browser

    finally:
        browser.quit()
        
    return browser
       

