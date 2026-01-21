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

        
        assert BASE_URL in driver.current_url, "Не загрузилась главная страница"

    def test_navigate_to_constructor_via_logo(self, driver):
        wait = WebDriverWait(driver, 15)
        driver.get(BASE_URL + PATHS["login"])


        
        login_page_element = wait.until(
            EC.presence_of_element_located(Locators.LOGIN_EMAIL_INPUT)
        )
        assert login_page_element.is_displayed(), "Поле email не отображается на странице входа"
        assert PATHS["login"] in driver.current_url, "Не загрузилась страница входа"

        
        logo = wait.until(
            EC.element_to_be_clickable(Locators.CONSTRUCTOR_LINK)
        )
        logo.click()

        
        wait.until(EC.url_contains(PATHS["main"]))
        assert PATHS["main"] in driver.current_url, "Не выполнен переход на главную страницу через логотип"

    def test_navigate_to_constructor_via_link(self, driver):
        wait = WebDriverWait(driver, 15)
        driver.get(BASE_URL + PATHS["main"])

        
        constructor_link = wait.until(
            EC.element_to_be_clickable(Locators.CONSTRUCTOR_LINK)
        )
        constructor_link.click()

        
        wait.until(EC.url_contains(PATHS["main"]))
        assert PATHS["main"] in driver.current_url, "Не выполнен переход через ссылку 'Конструктор'"