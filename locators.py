
from selenium.webdriver.common import by
By = by.By

class Locators:
    # Локаторы для входа
    LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")

    # Локатор для логотипа
    LOGOUT_BUTTON = (By.XPATH, "//a[@href='/']")

    # Локатор для ссылки «Конструктор»
    CONSTRUCTOR_LINK = (By.XPATH, "//nav//a[contains(text(), 'Конструктор')]")

    # Локатор для профиля (в шапке)
    PROFILE_LINK = (By.XPATH, "//a[contains(@href, 'account')]")

    # === КОНСТРУКТОР ===
    BUNS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab') and .//span[text()='Булки']]")
    SAUCES_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab') and .//span[text()='Соусы']]")
    INGREDIENTS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab') and .//span[text()='Начинки']]")
    BUNS_SECTION = (By.XPATH, "//section[contains(@class, 'BurgerIngredients') and contains(text(), 'Булки')]")
    SAUCES_SECTION = (By.XPATH, "//section[contains(@class, 'BurgerIngredients') and contains(text(), 'Соусы')]")
    INGREDIENTS_SECTION = (By.XPATH, "//section[contains(@class, 'BurgerIngredients') and contains(text(), 'Начинки')]")
    ACTIVE_TAB_INDICATOR = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")
    BASKET = (By.XPATH, "//section[@class='BurgerConstructor_basket_29Cd7 mt-25']")

    # === ФОРМА РЕГИСТРАЦИИ ===
    BUTTON_REGISTER = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")
    INPUT_NAME = (By.NAME, "name")
    INPUT_EMAIL = (By.NAME, "email")
    INPUT_PASSWORD = (By.NAME, "password")
    LINK_LOGIN_FROM_REGISTRATION = (By.XPATH, "//a[@href='/login' and contains(., 'Уже есть аккаунт')]")

    # === ФОРМА ВХОДА 
    INPUT_LOGIN_EMAIL = (By.XPATH, "//input[@name='email' and ancestor::form//button[contains(text(), 'Войти')]")
    INPUT_LOGIN_PASSWORD = (By.XPATH, "//input[@name='password' and ancestor::form//button[contains(text(), 'Войти')]")
    BUTTON_LOGIN_SUBMIT = (By.XPATH, "//button[contains(text(), 'Войти')]")

    # === ФОРМА ВОССТАНОВЛЕНИЯ ПАРОЛЯ ===
    INPUT_RESET_EMAIL = (By.XPATH, "//input[@name='email' and ancestor::form//button[contains(text(), 'Восстановить')]")
    BUTTON_RESET_SUBMIT = (By.XPATH, "//button[contains(text(), 'Восстановить')]")
    LINK_LOGIN_FROM_RESET = (By.XPATH, "//a[@href='/login' and contains(., 'Назад к логину')]")

    # === ОБЩИЕ ЭЛЕМЕНТЫ ФОРМ ===
    AUTH_FORM = (By.XPATH, "//form[.//button[contains(text(), 'Войти') or contains(text(), 'Зарегистрироваться') or contains(text(), 'Восстановить')]")
    AUTH_FIELD_SET = (By.XPATH, "//fieldset[parent::form[.//button[contains(text(), 'Войти')]]")
    PASSWORD_ERROR = (
        By.XPATH,
        "//div[contains(@class, 'error') or contains(text(), 'пароль') or contains(text(), '6')]"
    )