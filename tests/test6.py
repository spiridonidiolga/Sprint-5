def test_constructor_tabs(self):
    self.driver.get("https://stellar-burgers.test/constructor")
    # Переход в «Булки»
    self.driver.find_element(By.XPATH, locators.BUUNS_TAB).click()
    bun_element = self.driver.find_element(By.XPATH, "//h2[text()='Булки']")
    self.assertTrue(bun_element.is_displayed())

    # Переход в «Соусы»
    self.driver.find_element(By.XPATH, locators.SAUCES_TAB).click()
    sauce_element = self.driver.find_element(By.XPATH, "//h2[text()='Соусы']")
    self.assertTrue(sauce_element.is_displayed())
