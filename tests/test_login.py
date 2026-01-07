import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

class TestLogin:
    @pytest.mark.parametrize("scenario", [
        "main_page",
        "personal_account",
        "from_registration",
        "from_reset_password"
    ])
    def test_login_scenarios(self, driver, scenario):
        wait = WebDriverWait(driver, 15) 

        try:
            if scenario == "main_page":
                driver.get("https://stellarburgers.education-services.ru/")
                
                login_link = wait.until(
                    EC.element_to_be_clickable((
                        By.XPATH,
                        "//button[contains(@class, 'login-btn')] | "
                        "//a[contains(@href, 'login')] | "
                        "//*[contains(text(), 'Войти')]"
                    ))
                )
                login_link.click()

            elif scenario == "personal_account":
                driver.get("https://stellarburgers.education-services.ru/")
                personal_account = wait.until(
                    EC.element_to_be_clickable((
                        By.CSS_SELECTOR, "[href*='account'], a.account-link"))
                )
                personal_account.click()

            elif scenario == "from_registration":
                driver.get("https://stellarburgers.education-services.ru/register")
                login_link = wait.until(
                    EC.element_to_be_clickable((
                        By.XPATH, "//a[contains(@href, 'login')] | //*[contains(text(), 'Войти в аккаунт')]"))
                )
                login_link.click()

            elif scenario == "from_reset_password":
                driver.get("https://stellarburgers.education-services.ru/forgot-password")
                login_link = wait.until(
                    EC.element_to_be_clickable((
                        By.XPATH, "//a[contains(@href, 'login')] | //*[contains(text(), 'Войти в аккаунт')]"))
                )
                login_link.click()

        except (TimeoutException, NoSuchElementException) as e:
            print(f"Элемент не найден для сценария '{scenario}': {e}")
            print(f"Текущий URL: {driver.current_url}")
            print(f"Заголовок страницы: {driver.title}")
            driver.save_screenshot(f"error_{scenario}_{int(time.time())}.png")
            raise

        time.sleep(2) 
