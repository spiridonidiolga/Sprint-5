import pytest
from selenium.webdriver.common.by import By
import locators

class TestNavigation:
    def test_navigate_to_personal_account(self, driver):
        
        driver.get("https://stellar-burgers.test")
        driver.find_element(By.XPATH, locators.PERSONAL_ACCOUNT_LINK).click()
        assert "Личный кабинет" in driver.page_source

    def test_navigate_to_constructor_via_logo(self, driver):
        
        driver.get("https://stellar-burgers.test/account")
        driver.find_element(By.XPATH, locators.LOGO_LINK).click()
        assert "Конструктор" in driver.page_source

    def test_navigate_to_constructor_via_link(self, driver):
        
        driver.get("https://stellar-burgers.test/account")
        driver.find_element(By.XPATH, locators.CONSTRUCTOR_LINK).click()
        assert "Конструктор" in driver.page_source
