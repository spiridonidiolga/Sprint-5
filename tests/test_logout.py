import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators
import data

class TestLogout:
    def test_logout_from_account(self, driver):
        
        wait = WebDriverWait(driver, 30)

                
        wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

                
        email_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, locators.LOGIN_EMAIL_INPUT))
        )
        
        password_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, locators.LOGIN_PASSWORD_INPUT))
        )
        wait.until(EC.visibility_of(password_input))
        password_input.send_keys(data.TEST_USER["password"])


        login_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, locators.LOGIN_SUBMIT_BUTTON))
        )
        login_button.click()

        
        wait.until(EC.url_contains("/account"))

        
        profile_link = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, locators.PROFILE_LINK))
        )
        profile_link.click()
        wait.until(EC.url_contains("/account/profile"))


        logout_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, locators.LOGOUT_BUTTON))
        )
        logout_button.click()

        
        wait.until(EC.url_contains("/login"))
        login_form = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, locators.LOGIN_FORM))
        )
        assert login_form.is_displayed(), "Форма логина не появилась после выхода"
