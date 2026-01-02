def test_login_from_main_page(self):
    self.driver.get("https://stellar-burgers.test")
    self.driver.find_element(By.XPATH, locators.LOGIN_LINK).click()
    self.driver.find_element(By.XPATH, locators.LOGIN_EMAIL_INPUT).send_keys("olgaspiridonidi36333@yandex.ru")
    self.driver.find_element(By.XPATH, locators.LOGIN_PASSWORD_INPUT).send_keys("123456")
    self.driver.find_element(By.XPATH, locators.LOGIN_SUBMIT_BUTTON).click()
    self.assertIn("Личный кабинет", self.driver.page_source)
