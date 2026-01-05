import pytest
from selenium.webdriver.common.by import By
import locators

class TestLogin:
    @pytest.mark.parametrize("scenario", [
        "main_page",
        "personal_account",
        "from_registration",
        "from_reset_password"
    ])
    def test_login_scenarios(self, driver, scenario):
        
        if scenario == "main_page":
            driver.get("https://stellar-burgers.test")
            driver.find_element(By.XPATH, locators.LOGIN_LINK).click()
        elif scenario == "personal_account":
            driver.get("https://stellar-burgers.test")
            driver.find_element(By.XPATH, locators.PERSONAL_ACCOUNT_LINK).click()
        elif scenario == "from_registration":
            driver.get("https://stellar-burgers.test/register")
            driver.find_element(By.XPATH, locators.LOGIN_LINK).click()
        elif scenario == "from_reset_password":
            driver.get("https://stellar-burgers.test/forgot-password")
            driver.find_element(By.XPATH, locators.LOGIN_LINK).click()

        
        driver.find_element(By.XPATH, locators.LOGIN_EMAIL_INPUT).send_keys("olgaspiridonidi36333@yandex.ru")
        driver.find_element(By.XPATH, locators.LOGIN_PASSWORD_INPUT).send_keys("123456")
        driver.find_element(By.XPATH, locators.LOGIN_SUBMIT_BUTTON).click()

        assert "Личный кабинет" in driver.page_source

