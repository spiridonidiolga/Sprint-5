import pytest
from selenium.webdriver.common.by import By
import locators

class TestRegistration:
    def test_successful_registration(self, driver):
        
        driver.get("https://stellar-burgers.test/register")

        driver.find_element(By.XPATH, locators.REG_NAME_INPUT).send_keys("Ольга Спиридониди")
        driver.find_element(By.XPATH, locators.REG_EMAIL_INPUT).send_keys("olgaspiridonidi36333@yandex.ru")
        driver.find_element(By.XPATH, locators.REG_PASSWORD_INPUT).send_keys("123456")
        driver.find_element(By.XPATH, locators.REG_SUBMIT_BUTTON).click()

        assert "Личный кабинет" in driver.page_source

    def test_invalid_password_validation(self, driver):
        
        driver.get("https://stellar-burgers.test/register")

        driver.find_element(By.XPATH, locators.REG_PASSWORD_INPUT).send_keys("123")
        driver.find_element(By.XPATH, locators.REG_SUBMIT_BUTTON).click()

        error_element = driver.find_element(By.XPATH, locators.REG_ERROR_MESSAGE)
        assert error_element.is_displayed()
        assert "Пароль некорректный" in error_element.text


