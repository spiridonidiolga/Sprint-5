
from selenium.webdriver.common import by
By = by.By


class Locators:
    # Локаторы для входа
    LOGIN_EMAIL_INPUT = (By.XPATH, "//div/main/div/form/fieldset[1]/div/div/input")

    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    
    
    # Локатор для профиля (в шапке)
    PROFILE_LINK = (By.XPATH, "//a[contains(@href, 'account')]")
    LOGOUT_BUTTON = (By.XPATH, "//div/main/div/nav/ul/li[3]/button")
    

    # === КОНСТРУКТОР ===
    
    SAUCES_TAB = (By.XPATH, "//div/main/section[1]/div[1]/div[2]")
    INGREDIENTS_TAB = (By.XPATH, "//div/main/section[1]/div[1]/div[3]")
    
    SAUCES_SECTION = (By.XPATH, "//div/main/section[1]/div[2]")
    INGREDIENTS_SECTION = (By.XPATH, "//div/main/section[1]/div[2]")
    

    # === ФОРМА РЕГИСТРАЦИИ ===
    BUTTON_REGISTER = (By.XPATH, "//div/main/div/div/p[1]/a")
    INPUT_NAME = (By.XPATH, "//div/main/div/form/fieldset[1]/div/div/input")
    INPUT_EMAIL = (By.XPATH, "//div/main/div/form/fieldset[2]/div/div/input")
    INPUT_PASSWORD = (By.XPATH, "//div/main/div/form/fieldset[3]/div/div/input")
    
    LINK_LOGIN_FROM_REGISTRATION = (By.XPATH, "//a[@href='/login' and contains(., 'Уже есть аккаунт')]")

    # === ФОРМА ВХОДА 
    INPUT_LOGIN_EMAIL = (By.XPATH, "//input[@name='email' and ancestor::form//button[contains(text(), 'Войти')]")
    INPUT_LOGIN_PASSWORD = (By.XPATH, "//input[@name='password' and ancestor::form//button[contains(text(), 'Войти')]")
    BUTTON_LOGIN_SUBMIT = (By.XPATH, "//button[contains(text(), 'Войти')]")

    
    # === ОБЩИЕ ЭЛЕМЕНТЫ ФОРМ ===
    CONSTRUCTOR_LINK = (By.XPATH, "//div/header/nav/ul/li[1]/a/p")
    PASSWORD_ERROR = (
        By.XPATH,
        "//div[contains(@class, 'error') or contains(text(), 'пароль') or contains(text(), '6')]"
    )