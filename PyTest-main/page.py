from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Page:
    def __init__(self, browser, url):
        browser.get("https://www.work.ua/")
        self.browser = browser
        print(self.browser)
        
    def get_search_form(self):
        return self.browser.find_element_by_css_selector('#search')
    
    def get_main_search_label(self):
        return self.browser.find_element_by_css_selector('h1.text-basic.text-muted')
    
    def get_city_menu(self):
        return self.browser.find_element_by_css_selector("#city")
                                                    
    def search_in_city_menu(self, city):
        city_form = self.get_city_menu();
        city_form.clear()
        city_form.send_keys(city)
        self.get_search_form().send_keys(Keys.RETURN)                                                    
    
    def get_days_sort_menu(self):
        return self.get_main_search_label().find_element_by_css_selector(".glyphicon.glyphicon-chevron-down.glyph-indent")
    
    def get_7_days_sort(self):
        return self.browser.find_element_by_css_selector('[data-days="123"]')
    
    def get_result_announcements(self):
        return self.browser.find_element_by_css_selector('.text-muted.small')
    
