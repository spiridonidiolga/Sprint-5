import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import locators

class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellar-burgers.test/register")

    def test_successful_registration(self):
        
        self.driver.find_element(By.XPATH, locators.REG_NAME_INPUT).send_keys("Ольга Спиридониди")
        self.driver.find_element(By.XPATH, locators.REG_EMAIL_INPUT).send_keys("olgaspiridonidi36333@yandex.ru")
        self.driver.find_element(By.XPATH, locators.REG_PASSWORD_INPUT).send_keys("123456")
        self.driver.find_element(By.XPATH, locators.REG_SUBMIT_BUTTON).click()

        
        self.assertIn("Личный кабинет", self.driver.page_source)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
