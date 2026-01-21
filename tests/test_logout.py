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
from config import BASE_URL, PATHS

class TestLogout:

  def test_logout_from_account(self, driver):
    driver.get(BASE_URL + PATHS["login"])
    wait = WebDriverWait(driver, 30)


    
    email_input = wait.until(EC.element_to_be_clickable(Locators.LOGIN_EMAIL_INPUT))
    email_input.send_keys("spiridonidiolechka11@gmail.com")

    
    password_input = wait.until(EC.element_to_be_clickable(Locators.LOGIN_PASSWORD_INPUT))
    password_input.send_keys("111111")

    
    login_button = wait.until(EC.element_to_be_clickable(Locators.LOGIN_SUBMIT_BUTTON))
    login_button.click()

    
    profile_link = wait.until(EC.visibility_of_element_located(Locators.PROFILE_LINK))
    profile_link.click()

   
    wait.until(EC.url_contains("/account"))

   
    logout_button = wait.until(EC.element_to_be_clickable(Locators.LOGOUT_BUTTON))
    logout_button.click()

    
    wait.until(EC.url_contains("/login"))
    assert "/login" in driver.current_url, "После выхода пользователь не перенаправлен на страницу входа"
