import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import sys
sys.path.append(r"C:\Users\Я\Sprint-5")
import data
import sys
sys.path.append(r"C:\Users\Я\Sprint-5")
from locators import Locators

@pytest.mark.usefixtures("driver_init")
class TestConstructorTabs:

    def _click_tab_and_verify_active(self, tab_locator, expected_tab_text):
        
        tab = self.wait.until(EC.element_to_be_clickable(tab_locator))
        tab.click()

        
        new_element = self.wait.until(
            EC.presence_of_element_located(Locators.ACTIVE_TAB_INDICATOR)
        )
        assert new_element.is_displayed(), "Активный раздел присутствует в DOM, но не отображается"

        
        active_tab = self.wait.until(
            EC.visibility_of_element_located(Locators.ACTIVE_TAB_INDICATOR)
        )
        assert expected_tab_text in active_tab.text, (
            f"Ожидалась активная вкладка '{expected_tab_text}', "
            f"но активна: '{active_tab.text}'"
        )

    def test_bun_tab_scroll(self):
       
        new_element = self.wait.until(
            EC.presence_of_element_located(Locators.ACTIVE_TAB_INDICATOR)
        )
        assert new_element.is_displayed(), "Активный раздел присутствует в DOM, но не отображается"

        
        active_tab = self.wait.until(
            EC.visibility_of_element_located(Locators.ACTIVE_TAB_INDICATOR)
        )
        assert "Булки" in active_tab.text, "Вкладка «Булки» не подсвечена как активная"

    def test_sauce_tab_scroll(self):
        
        self._click_tab_and_verify_active(
            Locators.SAUCES_TAB,
            "Соусы"
        )
    def test_ingredient_tab_scroll(self):
        
        self._click_tab_and_verify_active(
            Locators.INGREDIENTS_TAB,
            "Начинки"
        )