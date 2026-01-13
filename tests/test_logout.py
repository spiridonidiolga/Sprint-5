import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
sys.path.append(r"C:\Users\Я\Sprint-5")
import data
import sys
sys.path.append(r"C:\Users\Я\Sprint-5")
from locators import Locators

class TestLogout:
    def test_logout_from_account(self, driver):
        driver.get("https://stellarburgers.education-services.ru/login")
        wait = WebDriverWait(driver, 30)
        wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

        email_input = wait.until(
            EC.presence_of_element_located(Locators.LOGIN_EMAIL_INPUT)
        )
        email_input.send_keys(data.TEST_USER["email"])
        password_input = wait.until(
            EC.presence_of_element_located(Locators.LOGIN_PASSWORD_INPUT)
        )
        password_input.send_keys(data.TEST_USER["password"])
        login_button = wait.until(
            EC.element_to_be_clickable(Locators.LOGIN_SUBMIT_BUTTON)
        )
        login_button.click()
        wait.until(EC.url_contains("/account"))
        profile_link = wait.until(
            EC.element_to_be_clickable(Locators.PROFILE_LINK)
        )
        profile_link.click()
        wait.until(EC.url_contains("/account/profile"))
        logout_button = wait.until(
            EC.element_to_be_clickable(Locators.LOGOUT_BUTTON)
        )
        logout_button.click()
        wait.until(EC.url_contains("/login"))
        login_form = wait.until(
            EC.presence_of_element_located(Locators.LOGIN_FORM)
        )
        assert login_form.is_displayed(), "Форма логина не появилась после выхода"
