def test_successful_registration(self, driver): Успешная регистрация с корректными данными.
def test_invalid_password_validation(self, driver): Валидация пароля: ошибка для < 6 символов.
def test_login_scenarios(self, driver, scenario): Проверка всех сценариев входа в аккаунт.
def test_navigate_to_personal_account(self, driver): Переход в личный кабинет по клику.
def test_navigate_to_constructor_via_logo(self, driver): Переход в конструктор через логотип.
def test_navigate_to_constructor_via_link(self, driver): Переход в конструктор по кнопке «Конструктор».
def test_logout_from_account(self, driver): Выход из аккаунта по кнопке «Выйти».    
def test_bun_tab_scroll(self): Проверяет переход к разделу «Булки».
def test_sauce_tab_scroll(self): Проверяет переход к разделу «Соусы».    
def test_ingredient_tab_scroll(self): Проверяет переход к разделу «Начинки».    