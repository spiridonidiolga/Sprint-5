
from selenium.webdriver.common import by
By = by.By

class Locators:
# ФОРМА РЕГИСТРАЦИИ
    BUTTON_REGISTER = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")
    INPUT_NAME = (By.XPATH, "//input[@name='name' and ancestor::form//button[contains(text(), 'Зарегистрироваться')]]")
    INPUT_EMAIL = (By.XPATH, "//input[@name='email' and ancestor::form//button[contains(text(), 'Зарегистрироваться')]]")
    INPUT_PASSWORD = (By.XPATH, "//input[@name='password' and ancestor::form//button[contains(text(), 'Зарегистрироваться')]]")
    LINK_LOGIN_FROM_REGISTRATION = (By.XPATH, "//a[@href='/login' and contains(., 'Уже есть аккаунт')]")

# ФОРМА ВХОДА
    INPUT_LOGIN_EMAIL = (By.XPATH, "//input[@name='email' and ancestor::form//button[contains(text(), 'Войти')]]")
    INPUT_LOGIN_PASSWORD = (By.XPATH, "//input[@name='password' and ancestor::form//button[contains(text(), 'Войти')]]")
    BUTTON_LOGIN_SUBMIT = (By.XPATH, "//button[contains(text(), 'Войти')]")

# ФОРМА ВОССТАНОВЛЕНИЯ ПАРОЛЯ
    INPUT_RESET_EMAIL = (By.XPATH, "//input[@name='email' and ancestor::form//button[contains(text(), 'Восстановить')]]")
    BUTTON_RESET_SUBMIT = (By.XPATH, "//button[contains(text(), 'Восстановить')]")
    LINK_LOGIN_FROM_RESET = (By.XPATH, "//a[@href='/login' and contains(., 'Назад к логину')]")

# ОБЩИЕ ЭЛЕМЕНТЫ ФОРМ
    AUTH_FORM = (By.XPATH, "//form[.//button[contains(text(), 'Войти') or contains(text(), 'Зарегистрироваться') or contains(text(), 'Восстановить')]]")
    AUTH_FIELD_SET = (By.XPATH, "//fieldset[parent::form[.//button[contains(text(), 'Войти')]]]")


# Форма входа
    LOGIN_EMAIL_INPUT = (By.XPATH, "//div/div/main/div/form/fieldset[1]/div/div/input")
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@type='password' and contains(@class, 'text_type_main-default')]")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//div/div/main/div/form/button")



# Профиль и выход
    PROFILE_LINK = (By.XPATH, "//a[contains(text(), 'Профиль')]")
    LOGOUT_BUTTON = (By.XPATH, "//div/div/main/div/nav/ul/li[3]/button")
    



    BUNS_TAB = (By.XPATH, "//section[@class='BurgerIngredients_ingredients_1N8v2']/child::*[contains(text(), 'Булки')]")
    SAUCES_TAB = (By.XPATH, "//section[@class='BurgerIngredients_ingredients_1N8v2']/child::*[contains(text(), 'Соусы')]")
    INGREDIENTS_TAB = (By.XPATH, "//section[@class='BurgerIngredients_ingredients_1N8v2']/child::*[contains(text(), 'Начинки')]")

    BUNS_SECTION = (By.XPATH, "//section[contains(@class, 'BurgerIngredients') and contains(text(), 'Булки')]")
    SAUCES_SECTION = (By.XPATH, "//section[contains(@class, 'BurgerIngredients') and contains(text(), 'Соусы')]")
    INGREDIENTS_SECTION = (By.XPATH, "//section[contains(@class, 'BurgerIngredients') and contains(text(), 'Начинки')]")

    ACTIVE_TAB = (By.XPATH, "//section[@class='BurgerIngredients_ingredients_1N8v2']/child::*[contains(@class, 'active')]")

    BASKET = (By.XPATH, "//section[@class='BurgerConstructor_basket_29Cd7 mt-25']")















