import pytest
from selenium.webdriver.common.by import By
import locators

class TestLogout:
    def test_logout_from_account(self, driver):
        
        driver.get("https://stellar-burgers.test/account")
