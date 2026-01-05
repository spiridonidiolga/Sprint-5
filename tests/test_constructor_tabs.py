import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators

class TestConstructorTabs:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellar-burgers.test/constructor")
        self.wait = WebDriverWait(self.driver, 10)
        yield
        self.driver.quit()  

    def test_bun_tab_scroll(self):
        
        bun_tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.BUUNS_TAB)))
        bun_tab.click()

        
        bun_section = self.wait.until(EC.visibility_of_element_located((By.XPATH, locators.BUUNS_SECTION)))
        assert bun_section.is_displayed(), "Раздел «Булки» не отображается после клика"

        
        active_tab = self.driver.find_element(By.XPATH, locators.ACTIVE_TAB_INDICATOR)
        assert "Булки" in active_tab.text, "Вкладка «Булки» не подсвечена как активная"

    def test_sauce_tab_scroll(self):
        
        sauce_tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.SAUCES_TAB)))
        sauce_tab.click()

        sauce_section = self.wait.until(EC.visibility_of_element_located((By.XPATH, locators.SAUCES_SECTION)))
        assert sauce_section.is_displayed(), "Раздел «Соусы» не отображается"

        active_tab = self.driver.find_element(By.XPATH, locators.ACTIVE_TAB_INDICATOR)
        assert "Соусы" in active_tab.text, "Вкладка «Соусы» не активна"

    def test_ingredient_tab_scroll(self):
        
        ingredient_tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.INGREDIENTS_TAB)))
        ingredient_tab.click()

        ingredient_section = self.wait.until(EC.visibility_of_element_located((By.XPATH, locators.INGREDIENTS_SECTION)))
        assert ingredient_section.is_displayed(), "Раздел «Начинки» не отображается"
        active_tab = self.driver.find_element(By.XPATH, locators.ACTIVE_TAB_INDICATOR)
        assert "Начинки" in active_tab.text, "Вкладка «Начинки» не активна"

    
