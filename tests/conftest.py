import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait



@pytest.fixture
def driver():
    
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)  

    yield driver
    driver.quit()  

@pytest.fixture
def wait(driver):
    
    return WebDriverWait(driver, 15)

@pytest.fixture(scope="class")
def driver_init(request):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://stellarburgers.education-services.ru/")
    wait = WebDriverWait(driver, 30)

    
    yield driver
    driver.quit()

