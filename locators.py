# --- Страница регистрации
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

# --- Общий интерфейс ---
PERSONAL_ACCOUNT_LINK = "//p[text()='Личный кабинет']"  # Ссылка «Личный кабинет»
LOGOUT_BUTTON = "//button[text()='Выйти']"  # Кнопка «Выйти»
LOGO_LINK = "//img[@alt='Stellar Burgers']"  # Логотип Stellar Burgers
CONSTRUCTOR_LINK = "//p[text()='Конструктор']"  # Ссылка «Конструктор»

# --- Раздел «Конструктор» ---
BUUNS_TAB = "//div[text()='Булки']"  # Вкладка «Булки»
SAUCES_TAB = "//div[text()='Соусы']"  # Вкладка «Соусы»
INGREDIENTS_TAB = "//div[text()='Начинки']"  # Вкладка «Начинки»
