
from selenium.webdriver.common import by
By = by.By


class Locators:
    # Локаторы для входа
   
    LOGIN_EMAIL_INPUT = (By.XPATH, "//fieldset[.//label[contains(text(), 'Email')]]//input")
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//fieldset[.//label[contains(text(), 'Пароль')]]//input[@type='password']")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[contains(., 'Войти')]")
    
    
    # Локатор для профиля (в шапке)
    PROFILE_LINK = (By.XPATH, "//a[contains(., 'Личный Кабинет')]")

    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

    
    # === КОНСТРУКТОР ===
    
     # Вкладки (Tabs)
    SAUCES_TAB = (By.XPATH, "//div[contains(@class, 'tab') and .//span[text()='Соусы']]")
    INGREDIENTS_TAB = (By.XPATH, "//div[contains(@class, 'tab') and .//span[text()='Начинки']]")

    # Секции (Sections)
    SAUCES_SECTION = (By.XPATH, "//section[contains(., 'Соусы')]")
    INGREDIENTS_SECTION = (By.XPATH, "//section[contains(., 'Начинки')]")
    

    # === ФОРМА РЕГИСТРАЦИИ ===
    BUTTON_REGISTER = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")



    INPUT_NAME = (By.XPATH, "//fieldset[.//label[contains(text(), 'Имя')]]//input")
    INPUT_EMAIL = (By.XPATH, "//fieldset[.//label[contains(text(), 'Email')]]//input")
    INPUT_PASSWORD = (By.XPATH, "//fieldset[.//label[contains(text(), 'Пароль')]]//input")
    
    
    # === ФОРМА ВХОДА 
    INPUT_LOGIN_EMAIL = (By.XPATH, "//fieldset[.//label[contains(text(), 'Email')]]//input")
    INPUT_LOGIN_PASSWORD = (By.XPATH, "//fieldset[.//label[contains(text(), 'Пароль')]]//input")
    BUTTON_LOGIN_SUBMIT = (By.XPATH, "//button[contains(., 'Войти') or contains(text(), 'Войти')]")
    
    # === ОБЩИЕ ЭЛЕМЕНТЫ ФОРМ ===
    CONSTRUCTOR_LINK = (By.XPATH, "//a[contains(., 'Конструктор') or .//p[contains(text(), 'Конструктор')]]")
    PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")




  