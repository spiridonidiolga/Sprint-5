
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL, PATHS
import sys
sys.path.append(r"C:\Users\Я\Sprint-5")
from locators import Locators
from helpers import click_tab_and_verify_section  

@pytest.mark.usefixtures("driver_init")
class TestConstructorTabs:

    def test_sauce_tab_scroll(self, driver):
        self.driver = driver
        wait = WebDriverWait(driver, 20)
        driver.get(BASE_URL + PATHS["main"])

        wait.until(
            EC.presence_of_element_located(Locators.CONSTRUCTOR_LINK),
        )

        
        click_tab_and_verify_section(
            driver,
            Locators.SAUCES_TAB,
            Locators.SAUCES_SECTION,
            "Соусы",
            "Соусы"
        )

       
        sauces_section = wait.until(
            EC.visibility_of_element_located(Locators.SAUCES_SECTION)
        )
        assert sauces_section.is_displayed(), "Секция «Соусы» не отображается после клика по вкладке"

    def test_ingredient_tab_scroll(self, driver):
        self.driver = driver
        wait = WebDriverWait(driver, 20)
        driver.get(BASE_URL + PATHS["main"])

        wait.until(
            EC.presence_of_element_located(Locators.CONSTRUCTOR_LINK),
            "Страница конструктора не загрузилась"
        )

        
        click_tab_and_verify_section(
            driver,
            Locators.INGREDIENTS_TAB,
            Locators.INGREDIENTS_SECTION,
            "Начинки",
            "Начинки"
        )

        
        ingredients_section = wait.until(
            EC.visibility_of_element_located(Locators.INGREDIENTS_SECTION)
        )
        assert ingredients_section.is_displayed(), "Секция «Начинки» не отображается после клика по вкладке"
