# --- Страница регистрации ---
REG_NAME_INPUT = "//input[@name='name']"  # Поле ввода имени
REG_EMAIL_INPUT = "//input[@name='email']"  # Поле ввода email
REG_PASSWORD_INPUT = "//input[@name='password']"  # Поле ввода пароля
REG_SUBMIT_BUTTON = "//button[text()='Зарегистрироваться']"  # Кнопка «Зарегистрироваться»
REG_ERROR_MESSAGE = "//div[contains(@class, 'error')]"  # Сообщение об ошибке

# --- Страница входа ---
LOGIN_EMAIL_INPUT = "//input[@name='email']"  # Поле email
LOGIN_PASSWORD_INPUT = "//input[@name='password']"  # Поле пароля
LOGIN_SUBMIT_BUTTON = "//button[text()='Войти']"  # Кнопка «Войти»
LOGIN_LINK = "//a[text()='Войти в аккаунт']"  # Ссылка «Войти в аккаунт» на главной
PERSONAL_ACCOUNT_LINK = "//p[text()='Личный кабинет']"  # Ссылка «Личный кабинет»

# --- Восстановление пароля ---
FORGOT_PASSWORD_LINK = "//a[text()='Забыли пароль?']"  # Ссылка «Забыли пароль?»
RESET_PASSWORD_BUTTON = "//button[text()='Восстановить']"  # Кнопка восстановления


# --- Общий интерфейс ---
LOGOUT_BUTTON = "//button[text()='Выйти']"  # Кнопка «Выйти»
LOGO_LINK = "//img[@alt='Stellar Burgers']"  # Логотип Stellar Burgers
CONSTRUCTOR_LINK = "//p[text()='Конструктор']"  # Ссылка «Конструктор»

# --- Раздел «Конструктор» ---
BUNS_TAB = "//div[text()='Булки']"  # Вкладка «Булки»
SAUCES_TAB = "//div[text()='Соусы']"  # Вкладка «Соусы»
INGREDIENTS_TAB = "//div[text()='Начинки']"  # Вкладка «Начинки»
TAB_CONTENT_HEADER = "//h2"  # Заголовок текущего раздела



INGREDIENTS_SECTION = "//section[@class='ingredients-section']"  # замените на корректный XPath

BUNS_TAB = "//div[contains(@class, 'tab') and contains(., 'Булки')]"
SAUCES_TAB = "//div[contains(@class, 'tab') and contains(., 'Соусы')]"
INGREDIENTS_TAB = "//div[contains(@class, 'tab') and contains(., 'Начинки')]"

