def test_logout(self):
    self.driver.get("https://stellar-burgers.test/account")
    self.driver.find_element(By.XPATH, locators.LOGOUT_BUTTON).click()
    self.assertIn("Войти", self.driver.page_source)
