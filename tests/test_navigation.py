import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL, PATHS
import sys
sys.path.append(r"C:\Users\Я\Sprint-5")
from locators import Locators

class TestNavigation:
    def test_navigate_to_personal_account(self, driver):
        wait = WebDriverWait(driver, 15)
        driver.get(BASE_URL + PATHS["main"])

        
        main_page_element = wait.until(
            EC.presence_of_element_located(Locators.CONSTRUCTOR_LINK)
        )
        assert main_page_element.is_displayed(), "Элемент 'Конструктор' не отображается на главной странице"
        assert "/main" in driver.current_url, "Не загрузилась главная страница"

        self._perform_login(driver, wait)

        
        personal_account = wait.until(
            EC.element_to_be_clickable(Locators.PROFILE_LINK)
        )
        assert personal_account.is_displayed(), "Ссылка 'Личный кабинет' не отображается"
        personal_account.click()

        
        wait.until(EC.url_contains("/account"))
        assert "/account" in driver.current_url, "Не произошёл переход в личный кабинет"

    def _perform_login(self, driver, wait):
        
        email_input = wait.until(
            EC.presence_of_element_located(Locators.LOGIN_EMAIL_INPUT)
        )
        assert email_input.is_enabled(), "Поле email недоступно для ввода"
        email_input.clear()
        email_input.send_keys("spiridonidiolechka11@gmail.com")

        
        password_input = wait.until(
            EC.presence_of_element_located(Locators.LOGIN_PASSWORD_INPUT)
        )
        assert password_input.is_enabled(), "Поле пароля недоступно для ввода"
        password_input.clear()
        password_input.send_keys("111111")

        
        login_button = wait.until(
            EC.element_to_be_clickable(Locators.LOGIN_SUBMIT_BUTTON)
        )
        assert login_button.is_displayed(), "Кнопка 'Войти' не отображается"
        login_button.click()

        
        wait.until(EC.url_contains("/"))
        assert "/" in driver.current_url, "Не удалось войти в аккаунт"

    def test_navigate_to_constructor_via_logo(self, driver):
        wait = WebDriverWait(driver, 15)
        driver.get(BASE_URL + PATHS["login"])

        
        login_page_element = wait.until(
            EC.presence_of_element_located(Locators.LOGIN_EMAIL_INPUT)
        )
        assert login_page_element.is_displayed(), "Поле email не отображается на странице входа"
        assert "/login" in driver.current_url, "Не загрузилась страница входа"

        
        logo = wait.until(
            EC.element_to_be_clickable(Locators.LOGOUT_BUTTON)  
        )
        assert logo.is_displayed(), "Логотип не отображается"
        logo.click()

       
        wait.until(EC.url_to_be(BASE_URL + PATHS["main"]))
        assert driver.current_url == BASE_URL + PATHS["main"], "Не произошёл переход на главную через логотип"


    def test_navigate_to_constructor_via_link(self, driver):
        wait = WebDriverWait(driver, 15)
        driver.get(BASE_URL + PATHS["main"])  

        
        main_page_element = wait.until(
            EC.presence_of_element_located(Locators.CONSTRUCTOR_LINK)
        )
        assert main_page_element.is_displayed(), "Ссылка 'Конструктор' не отображается на главной"
        assert "/main" in driver.current_url, "Не загрузилась главная страница"


        
        constructor_link = wait.until(
            EC.element_to_be_clickable(Locators.CONSTRUCTOR_LINK)
        )
        assert constructor_link.is_displayed(), "Ссылка 'Конструктор' не отображается"
        constructor_link.click()


        
        
