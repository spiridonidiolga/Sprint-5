import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class TestNavigation:
    def test_navigate_to_personal_account(self, driver):
        wait = WebDriverWait(driver, 15)

        
        driver.get("https://stellarburgers.education-services.ru/")

        try:
            
            wait.until(EC.url_contains("/login"))

            
            self._perform_login(driver, wait)

            
            personal_account = wait.until(
                EC.element_to_be_clickable((
                    By.XPATH,
            "//a[contains(@href, 'account')] | "
            "//button[contains(., 'Личный кабинет')] | "
            "//*[contains(., 'Профиль')] | "
            "//div[contains(@class, 'account')]"
        ))
            )
            personal_account.click()

            
            wait.until(EC.url_contains("/account"))

        except TimeoutException as e:
            self._handle_failure(driver, "Не удалось перейти в личный кабинет", e)
            raise

    def _perform_login(self, driver, wait):
        """Выполняет вход в систему с тестовыми данными"""
        try:
            
            email_input = wait.until(
                EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))
            )
            email_input.clear()
            email_input.send_keys("olgaspiridonidi36444@example.com")

            
            password_input = wait.until(
                EC.presence_of_element_located((By.XPATH, "//input[@type='password']"))
            )
            password_input.clear()
            password_input.send_keys("1730987654")


            
            login_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Войти')]"))
            )
            login_button.click()

            
            wait.until(EC.url_contains("/"))

        except TimeoutException as e:
            self._handle_failure(driver, "Ошибка при входе в систему", e)
            raise

    def test_navigate_to_constructor_via_logo(self, driver):
        """Тест навигации через логотип"""
        wait = WebDriverWait(driver, 15)
        driver.get("https://stellarburgers.education-services.ru/login")
        try:
            logo = wait.until(
                EC.element_to_be_clickable((
            By.XPATH,
            "//a[@href='/'] | "
            "//img[contains(@src, 'logo')] | "
            "//svg[contains(@class, 'logo')] | "
            "//div[contains(@class, 'logo')]"
        ))
            )
            logo.click()
            wait.until(EC.url_to_be("https://stellarburgers.education-services.ru/"))
        except TimeoutException as e:
            self._handle_failure(driver, "Логотип не найден", e)
            raise

    def test_navigate_to_constructor_via_link(self, driver):
        """Тест навигации через ссылку «Конструктор»"""
        wait = WebDriverWait(driver, 15)
        driver.get("https://stellarburgers.education-services.ru/")
        try:
            constructor_link = wait.until(
                EC.element_to_be_clickable((
            By.XPATH,
            "//a[contains(., 'Конструктор')] | "
            "//nav//a[contains(., 'Конструктор')] | "
            "//*[contains(., 'Конструктор бургеров')] | "
            "//li[contains(., 'Конструктор')]"
        ))
            )
            constructor_link.click()
            wait.until(EC.url_contains("/"))
        except TimeoutException as e:
            self._handle_failure(driver, "Ссылка «Конструктор» не найдена", e)
            raise

    
