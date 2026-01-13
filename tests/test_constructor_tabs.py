import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from locators import Locators



class TestConstructorTabs:
    def setup_method(self):
        """Настройка драйвера перед каждым тестом"""
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://stellarburgers.education-services.ru/")
        self.wait = WebDriverWait(self.driver, 10)

    def teardown_method(self):
        """Очистка после каждого теста (закрытие браузера)"""
        self.driver.quit()

    def _click_tab_and_verify_section(self, tab_locator, section_locator, tab_name, section_name):
        
        tab = self.wait.until(EC.element_to_be_clickable(tab_locator))
        tab.click()
       
    
        section = self.wait.until(EC.presence_of_element_located(section_locator))
        print(f"Секция '{section_name}' найдена")

       
        assert section.text == section_name, f"Ожидалось '{section_name}', но секция содержит '{section.text}'"
        

    def test_bun_tab_scroll(self):
        
        self._click_tab_and_verify_section(
            Locators.BUNS_TAB,
            Locators.BUNS_SECTION,
            "Булки",
            "Булки"
        )

    def test_sauce_tab_scroll(self):
        
        self._click_tab_and_verify_section(
            Locators.SAUCES_TAB,
            Locators.SAUCES_SECTION,
            "Соусы",
            "Соусы"
        )

    def test_ingredient_tab_scroll(self):
        
        self._click_tab_and_verify_section(
            Locators.INGREDIENTS_TAB,
            Locators.INGREDIENTS_SECTION,
            "Начинки",
            "Начинки"
        )  



