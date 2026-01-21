from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import sys

sys.path.append(r"C:\Users\Я\Sprint-5")

import data
from locators import Locators
from helpers import fill_registration_form, wait_for_password_error

class TestStellarBurgersRegistration:
    BASE_URL = "https://stellarburgers.education-services.ru"

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 30)

    def teardown_method(self):
        self.driver.quit()

    @pytest.mark.parametrize("test_data", [data.TEST_DATA["valid"]])
    def test_successful_registration(self, test_data):
        self.driver.get(f"{self.BASE_URL}/register")

        fill_registration_form(
            self.driver,
            self.wait,
            Locators,
            name=test_data["name"],
            email=test_data["email"],
            password=test_data["password"]
        )

        register_button = self.wait.until(
            EC.element_to_be_clickable(Locators.BUTTON_REGISTER)
        )
        register_button.click()

        self.wait.until(EC.url_contains("/login"))
        assert "/login" in self.driver.current_url, "Не произошёл переход на страницу входа после регистрации"

    @pytest.mark.parametrize("test_data", [data.TEST_DATA["short_password"]])
    def test_invalid_password_validation(self, test_data):
        self.driver.get(f"{self.BASE_URL}/register")

        fill_registration_form(
            self.driver,
            self.wait,
            Locators,
            name=test_data["name"],
            email=test_data["email"],
            password=test_data["password"]
        )

        register_button = self.wait.until(
            EC.element_to_be_clickable(Locators.BUTTON_REGISTER)
        )
        register_button.click()

        
        error_element = wait_for_password_error(self.driver, self.wait, Locators)

        
        assert error_element.is_displayed(), "Сообщение об ошибке не отображается на странице"
        assert len(error_element.text.strip()) > 0, "Сообщение об ошибке пустое"
        assert "/login" not in self.driver.current_url, "Переход на страницу входа произошёл несмотря на ошибку"
