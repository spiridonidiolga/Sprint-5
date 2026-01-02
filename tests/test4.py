def test_navigate_to_constructor_via_logo(self):
    self.driver.get("https://stellar-burgers.test/account")
    self.driver.find_element(By.XPATH, locators.LOGO_LINK).click()
    self.assertIn("Конструктор", self.driver.page_source)
