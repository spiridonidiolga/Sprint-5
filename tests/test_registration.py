from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

class TestStellarBurgersRegistration:
    BASE_URL = "https://stellarburgers.education-services.ru" 

    def setup_method(self):
       
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 30)

    def teardown_method(self):
        
        self.driver.quit()

    def _fill_registration_form(self, name, email, password):
        
        name_input = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Имя' or @name='name']"))
        )
        name_input.clear()
        name_input.send_keys(name)

        
        email_input = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='email' or @placeholder='Email' or @name='email']"))
        )
        email_input.clear()
        email_input.send_keys(email)

        
        password_input = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='password' or @placeholder='Пароль' or @name='password']"))
        )
        password_input.clear()
        password_input.send_keys(password)

    def _wait_for_password_error(self):
       
        error_element = self.wait.until(
            EC.visibility_of_element_located((
                By.XPATH,
                "//p[contains(text(), 'Некорректный пароль')] | "
                "//div[contains(text(), 'минимум 6 символов')] | "
                "//span[contains(text(), 'пароль')] | "
                "//*[contains(text(), '6 символов')]"
            ))
        )

        error_text = error_element.text.lower()
        assert any([
            "6" in error_text,
            "пароль" in error_text,
            "минимум 6" in error_text,
            "некорректный" in error_text,
            "символов" in error_text
        ]), (
            f"Сообщение об ошибке не соответствует ожиданиям. "
            f"Фактический текст: '{error_text}'"
        )
        return error_element

    def test_successful_registration(self):
        
        self.driver.get(f"{self.BASE_URL}/register")

        
        self._fill_registration_form(
            name="Тестовый Пользователь",
            email="testuser123@ya.ru",
            password="SecurePass123"
        )

        register_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Зарегистрироваться') or @type='submit']"))
        )
        register_button.click()

        self.wait.until(EC.url_contains("/login"))
        assert "/login" in self.driver.current_url, "Не произошёл переход на страницу входа после регистрации"

    def test_invalid_password_validation(self):
       
        self.driver.get(f"{self.BASE_URL}/register")
       

        self._fill_registration_form(
            name="Тестовый Пользователь",
            email="testuser456@ya.ru",
            password="123" 
        )

        register_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Зарегистрироваться') or @type='submit']"))
        )
        register_button.click()

        error_element = self._wait_for_password_error()
        assert error_element.is_displayed(), "Сообщение об ошибке не отображается на странице"
        assert len(error_element.text.strip()) > 0, "Сообщение об ошибки пустое"
