import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL, PATHS
import sys
sys.path.append(r"C:\Users\Я\Sprint-5")
from helpers import wait_and_click, assert_url_contains



class TestLogin:
    def setup_method(self):
        self.driver = webdriver.Chrome()

    def teardown_method(self):
        self.driver.quit()

    def test_login_from_main_page(self):
        self.driver.get(BASE_URL + PATHS["main"])

        login_button = wait_and_click(
            self.driver,
            "//button[contains(@class, 'login-btn')] | "
            "//a[contains(@href, 'login')] | "
            "//*[contains(text(), 'Войти')]",
            "xpath"
        )
        assert login_button is not None, "Кнопка входа не найдена на главной странице"
        assert_url_contains(self.driver, '/login')


    def test_login_from_personal_account(self):
        self.driver.get(BASE_URL + PATHS["main"])

        
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, ".Modal_modal_overlay__x2ZCr"))
        )

        account_link = wait_and_click(
            self.driver,
            "[href*='account'], a.account-link",
            "css"
        )
        assert account_link is not None, "Ссылка личного кабинета не найдена на главной странице"
        assert_url_contains(self.driver, '/login')

    def test_login_from_registration_page(self):
        self.driver.get(BASE_URL + PATHS["register"])
        login_link = wait_and_click(
            self.driver,
            "//a[contains(@href, 'login')] | //*[contains(text(), 'Войти в аккаунт')]",
            "xpath"
        )
        assert login_link is not None, "Ссылка входа не найдена на странице регистрации"
        assert_url_contains(self.driver, '/login')

    def test_login_from_reset_password_page(self):
        self.driver.get(BASE_URL + PATHS["forgot-password"])

        login_link = wait_and_click(
            self.driver,
            "//a[contains(@href, 'login')] | //*[contains(text(), 'Войти в аккаунт')]",
            "xpath"
        )
        assert login_link is not None, "Ссылка входа не найдена на странице восстановления пароля"
        assert_url_contains(self.driver, '/login')