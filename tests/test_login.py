import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL, PATHS


class TestLogin:
    def setup_method(self):
       
        self.driver = webdriver.Chrome()  
        self.wait = WebDriverWait(self.driver, 15)

    def teardown_method(self):
       
        self.driver.quit()


    def _wait_and_click(self, locator, locator_type=By.XPATH):
        
        element = self.wait.until(EC.element_to_be_clickable((locator_type, locator)))
        element.click()
        return element

    def _assert_url_contains(self, expected_substring, timeout=10):
        
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(expected_substring)
        )
        assert expected_substring in self.driver.current_url, \
            f"Ожидалось, что URL содержит '{expected_substring}', но текущий URL: {self.driver.current_url}"

    def test_login_from_main_page(self):
        
        self.driver.get(BASE_URL + PATHS["main"])


        
        self._wait_and_click(
            "//button[contains(@class, 'login-btn')] | "
            "//a[contains(@href, 'login')] | "
            "//*[contains(text(), 'Войти')]",
            By.XPATH
        )

        
        self._assert_url_contains('/login')

    def test_login_from_personal_account(self):
        
        self.driver.get(BASE_URL + PATHS["main"])


        
        self._wait_and_click("[href*='account'], a.account-link", By.CSS_SELECTOR)

        
        self._assert_url_contains('/login')

    def test_login_from_registration_page(self):
        
        self.driver.get(BASE_URL + PATHS["register"])


        
        self._wait_and_click(
            "//a[contains(@href, 'login')] | //*[contains(text(), 'Войти в аккаунт')]",
            By.XPATH
        )

       
        self._assert_url_contains('/login')

    def test_login_from_reset_password_page(self):
    
        self.driver.get(BASE_URL + PATHS["forgot-password"])

       
        self._wait_and_click(
            "//a[contains(@href, 'login')] | //*[contains(text(), 'Войти в аккаунт')]",
            By.XPATH
        )

       
        self._assert_url_contains('/login')
