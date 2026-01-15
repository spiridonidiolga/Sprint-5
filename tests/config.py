
BASE_URLS = {
    "prod": "https://stellarburgers.education-services.ru",
    "stage": "https://stage.stellarburgers.education-services.ru",
    "dev": "https://dev.stellarburgers.education-services.ru"
}



CURRENT_ENV = "prod"



BASE_URL = BASE_URLS[CURRENT_ENV]


PATHS = {
    "main": "/",
    "login": "/login",
    "register": "/register",
    "account": "/account",
    "constructor": "/constructor",
    "forgot-password": "/forgot-password"
}
