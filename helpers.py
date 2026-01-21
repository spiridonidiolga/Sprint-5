from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
LOCATOR_TYPES = {
    "xpath": By.XPATH,
    "css": By.CSS_SELECTOR,
}

def click_tab_and_verify_section(driver, tab_locator, section_locator, tab_name, section_name, timeout=20):
    
    wait = WebDriverWait(driver, timeout)

    
    tab_element = wait.until(
        EC.element_to_be_clickable(tab_locator),
        f"Вкладка '{tab_name}' не кликабельна или не найдена"
    )
    tab_element.click()

    
    section_element = wait.until(
        EC.visibility_of_element_located(section_locator),
        f"Секция '{section_name}' не появилась после клика на вкладку '{tab_name}'"
    )
    assert section_element.is_displayed(), f"Секция '{section_name}' найдена, но не отображается"




def wait_and_click(driver, locator, locator_type="xpath", timeout=15):
    
    wait = WebDriverWait(driver, timeout)
   
    by_type = LOCATOR_TYPES[locator_type.lower()]
    element = wait.until(EC.element_to_be_clickable((by_type, locator)))
    element.click()
    return element


def assert_url_contains(driver, expected_substring, message=None, timeout=10):
   
    WebDriverWait(driver, timeout).until(
        EC.url_contains(expected_substring)
    )
    current_url = driver.current_url
    
    final_message = message or f"Ожидалось, что URL содержит '{expected_substring}', но текущий URL: {current_url}"
    assert expected_substring in current_url, final_message



def fill_registration_form(driver, wait, locators, name, email, password):
    
    name_input = wait.until(
        EC.element_to_be_clickable(locators.INPUT_NAME)
    )
    assert name_input is not None, "Поле «Имя» не найдено на странице регистрации"
    name_input.clear()
    name_input.send_keys(name)
    assert name_input.get_attribute("value") == name, \
        f"В поле «Имя» ожидалось значение '{name}', но установлено '{name_input.get_attribute('value')}'"

    email_input = wait.until(
        EC.element_to_be_clickable(locators.INPUT_EMAIL)
    )
    assert email_input is not None, "Поле «Email» не найдено на странице регистрации"
    email_input.clear()
    email_input.send_keys(email)
    assert email_input.get_attribute("value") == email, \
        f"В поле «Email» ожидалось значение '{email}', но установлено '{email_input.get_attribute('value')}'"

    password_input = wait.until(
        EC.element_to_be_clickable(locators.INPUT_PASSWORD)
    )
    assert password_input is not None, "Поле «Пароль» не найдено на странице регистрации"
    password_input.clear()
    password_input.send_keys(password)
    assert password_input.get_attribute("value") == password, \
        f"В поле «Пароль» ожидалось значение '{password}', но установлено '{password_input.get_attribute('value')}'"

def wait_for_password_error(driver, wait, locators):
    
    error_element = wait.until(
        EC.visibility_of_element_located(locators.PASSWORD_ERROR),
        message="Не удалось найти видимый элемент с сообщением об ошибке пароля"
    )

    
    assert error_element is not None, "Элемент с сообщением об ошибке не найден"
    assert error_element.is_displayed(), "Элемент с сообщением об ошибке не виден на странице"
    assert len(error_element.text.strip()) > 0, "Текст сообщения об ошибке пуст"

    
    expected_error_text = "Некорректный пароль"  
    assert expected_error_text in error_element.text, f"Текст ошибки не соответствует ожидаемому. Ожидали: '{expected_error_text}', получили: '{error_element.text}'"

    

    return error_element

    