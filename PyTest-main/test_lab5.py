import pytest
import time
from page import Page
from selenium.webdriver.common.keys import Keys
import allure
    
@allure.suite("City form result test")
@allure.story("test suit for lab 5")      
def test_search_form(browser):
    search_string = "C#"
    
    with allure.step("finding " + search_string):
        search_form = pytest.page.get_search_form()
        search_form.send_keys(search_string)
        search_form.send_keys(Keys.RETURN)
        
    with allure.step("Checking main lanel after sarch"):    
        actual_result = pytest.page.get_main_search_label().text
        assert search_string in actual_result


@allure.suite("City form result test")
@allure.story("test suit for lab 5")
def test_city_form(browser):
    with allure.step("finding Дніпро vacancies"):
        pytest.page.search_in_city_menu("Дніпро")
        time.sleep(1)
        
    with allure.step("Checking main label after search"):
        
        actual_value = pytest.page.get_main_search_label().text
                     
        assert "Дніпр" in actual_value
                         
                                               
@allure.suite("Check sorting by date")
@allure.story("test suit for lab 5")
def test_sorting_by_date(browser):
        
    with allure.step("sorting by date in 7 dayperiod"):
        pytest.page.get_days_sort_menu().click()
        pytest.page.get_7_days_sort().click()
        actual_value = pytest.page.get_result_announcements().text
    
    with allure.step("Checking result if it in 7 days range"):
        seven_days = {"вчора","2","3","4","5","6","7"}
        result = ""
    
        for i in seven_days:
            if(i in actual_value):
                result = i
    
        time.sleep(2)
        assert result != ""
        
