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

@pytest.mark.usefixtures("driver_init")
class TestConstructorTabs:

    def _click_tab_and_verify_section(self, tab_locator, section_locator, tab_name, section_name):
        
        driver = self.driver
        wait = WebDriverWait(driver, 20)  

        
        tab_element = wait.until(
            EC.element_to_be_clickable(tab_locator),
            f"Вкладка '{tab_name}' не кликабельна или не найдена"
        )
        tab_element.click()

        
        section_element = wait.until(
            EC.visibility_of_element_located(section_locator),
            f"Секция '{section_name}' не появилась после клика на вкладку '{tab_name}'"
        )
        assert section_element.is_displayed(), f"Секция '{section_name}' найдена, но не отображается"

    def test_sauce_tab_scroll(self, driver):
        
        self.driver = driver
        wait = WebDriverWait(driver, 20)
        driver.get(BASE_URL + PATHS["main"])

        
        wait.until(
            EC.presence_of_element_located(Locators.CONSTRUCTOR_LINK),
           
        )

        self._click_tab_and_verify_section(
            Locators.SAUCES_TAB,
            Locators.SAUCES_SECTION,
            "Соусы",
            "Соусы"
        )

    def test_ingredient_tab_scroll(self, driver):
       
        self.driver = driver
        wait = WebDriverWait(driver, 20)
        driver.get(BASE_URL + PATHS["main"])

        
        wait.until(
            EC.presence_of_element_located(Locators.CONSTRUCTOR_LINK),
            "Страница конструктора не загрузилась"
        )

        self._click_tab_and_verify_section(
            Locators.INGREDIENTS_TAB,
            Locators.INGREDIENTS_SECTION,
            "Начинки",
            "Начинки"
        )