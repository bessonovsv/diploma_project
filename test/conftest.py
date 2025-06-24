"""
Фикстуры для тестов с использованием Selenium и HTTP-запросов.

Модуль определяет базовые фикстуры для запуска тестов, включающие:
- Создание HTTP-сессии с необходимыми заголовками
и cookie для отправки запросов к API.
- Управление браузером Firefox с помощью Selenium для выполнения UI-тестов.

Фикстуры предназначены для многократного использования в тестах
и управляют жизненным циклом соответствующих ресурсов.

Фикстуры:
- session(): Создает и возвращает HTTP-сессию с установленными
заголовками и куками.
- browser(): Запускает и управляет экземпляром браузера Firefox,
обеспечивая доступ к нему для UI-тестов.

Предназначение:
- Позволяет организовывать тестирование с минимальной ручной подготовкой и
освобождать ресурсы после завершения тестов.
"""

import pytest
import requests

from settings import HEADERS, COOKIES
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="session")
def session():
    """Создает сессию HTTP-клиента с заданными заголовками и куки.

    Возвращаемая сессия используется для отправки запросов к серверу.

    Yields:
        requests.session: объект сессии с настроенными заголовками и cookies.
    """

    s = requests.Session()
    s.headers.update(HEADERS)
    s.cookies.update(COOKIES)
    return s


@pytest.fixture(scope="function")
def browser(request):
    """Запускает браузер Firefox для текущего теста и
    закрывает его после завершения.

    Используется для управления браузером Selenium.

    Args:
        request: объект request pytest, содержащий дополнительную
        информацию о тестовом сценарии.

    Yields:
        webdriver.firefox: экземпляр браузера Firefox, готовый к
        использованию в тестах.
    """

    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()
