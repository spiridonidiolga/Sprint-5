import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class TestRegistration:
    def test_successful_registration(self, driver):
        wait = WebDriverWait(driver, 15)
        driver.get("https://stellarburgers.education-services.ru/register")

        try:
            
            name_input = wait.until(
                EC.presence_of_element_located((
                    By.XPATH,
            "//input[contains(@placeholder, 'Имя')] | "
            "//input[@placeholder='Имя'] | "
            "//input[@type='text']"
        ))
            )
            name_input.send_keys()

            
            email_input = wait.until(
                EC.presence_of_element_located((
            By.XPATH,
            "//input[contains(@placeholder, 'Email')] | "
            "//input[@placeholder='Email'] | "
            "//input[@type='email']"
        ))
            )
            email_input.send_keys()

            
            password_input = wait.until(
                EC.presence_of_element_located((
            By.XPATH,
            "//input[contains(@placeholder, 'Пароль')] | "
            "//input[@placeholder='Пароль'] | "
            "//input[@type='password']"
        ))
            )
            password_input.send_keys()

            
            register_button = wait.until(
                EC.element_to_be_clickable((
            By.XPATH,
            "//button[contains(., 'Зарегистрироваться')] | "
            "//button[@type='submit']"
        ))
            )
            register_button.click()

            
            wait.until(EC.url_contains("/login"))

        except TimeoutException as e:
            self._handle_failure(driver, "Ошибка при регистрации", e)
            raise


    def test_invalid_password_validation(self, driver):
        """Тест валидации пароля (менее 6 символов)"""
        wait = WebDriverWait(driver, 15)
        driver.get("https://stellarburgers.education-services.ru/register")

        try:
            
            name_input = wait.until(
                EC.presence_of_element_located((By.XPATH, "//input[contains(@placeholder, 'Имя')]"))
            )
            name_input.send_keys("Тестовый Пользователь")


            
            email_input = wait.until(
                EC.presence_of_element_located((By.XPATH, "//input[contains(@placeholder, 'Email')]"))
            )
            email_input.send_keys("test@example.com")

            
            password_input = wait.until(
                EC.presence_of_element_located((By.XPATH, "//input[contains(@placeholder, 'Пароль')]"))
            )
            password_input.send_keys("123")  


            
            register_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Зарегистрироваться')]"))
            )
            register_button.click()

            
            error_message = wait.until(
                EC.visibility_of_element_located((
            By.XPATH,
            "//p[contains(., 'Некорректный пароль')] | "
            "//div[contains(., 'Пароль')] | "
            "//span[contains(., 'минимум 6 символов')]"
        ))
            )
            assert "6" in errormessage.text or "пароль" in errormessage.text.lower(), \
                f"Ожидалось сообщение о пароле, но найдено: {errormessage.text}"

        except TimeoutException as e:
            self._handle_failure(driver, "Валидация пароля не сработала", e)
            raise

    def _handle_failure(self, driver, message, exception=None):
        """Вспомогательный метод для диагностики ошибок"""
        print(f"ОШИБКА: {message}")
        print(f"Текущий URL: {driver.current_url}")
        print(f"Заголовок страницы: {driver.title}")
        if exception:
            print(f"Исключение: {exception}")
        timestamp = int(time.time())
        driver.save_screenshot(f"error_{timestamp}.png")



