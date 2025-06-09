import pytest
import requests
from settings import HEADERS, COOKIES
from selenium import webdriver


@pytest.fixture(scope='session')
def session():
    s = requests.Session()
    s.headers.update(HEADERS)
    s.cookies.update(COOKIES)
    return s

from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(scope='function')
def browser():
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()
#@pytest.fixture(scope='function')
#def browser():
    # Создаем экземпляр драйвера Chrome
    #driver = webdriver.Chrome()
    #driver.maximize_window()
    #yield driver
    # После выполнения теста закрываем браузер
    #driver.quit()

