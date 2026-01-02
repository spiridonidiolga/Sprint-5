def test_invalid_password_validation(self):
    self.driver.find_element(By.XPATH, locators.REG_PASSWORD_INPUT).send_keys("123")
    self.driver.find_element(By.XPATH, locators.REG_SUBMIT_BUTTON).click()
    error_element = self.driver.find_element(By.XPATH, locators.REG_ERROR_MESSAGE)
    self.assertTrue(error_element.is_displayed())
    self.assertIn("Пароль некорректный", error_element.text)
