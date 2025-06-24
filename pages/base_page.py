"""
Модуль base_page.py

Этот модуль определяет базовую страницу (`BasePage`)
для взаимодействия с элементами веб-интерфейса.
Используется совместно с Selenium для автоматизации
тестирования веб-приложений.

Импортируемые модули:
- `By`: используется для выбора элементов на странице
различными способами (id, class name, xpath и др.).
- `WebDriverWait`: применяется для ожидания появления элемента на странице.
- `expected_conditions`: набор предопределенных условий
для проверки состояния страницы.
- `Tuple`: импорт типа данных Tuple для аннотаций типов.

Класс:
- `BasePage`: Базовый класс для всех страниц приложения,
содержащий общие методы и свойства,
такие как ожидание загрузки страницы и работа с элементами.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Tuple


class BasePage:
    """Базовая страница для взаимодействия с элементами веб-интерфейса."""

    def __init__(self, browser) -> None:
        """
        Конструктор класса базовой страницы.

        :param browser: Драйвер браузера (ChromeDriver, FirefoxDriver и т.д.).
        """
        self.browser = browser

    def open(self, url: str) -> None:
        """
        Открывает заданный URL в браузере.

        :param url: Адрес страницы для открытия.
        """
        self.browser.get(url)

    def wait_for_element(
            self, locator: Tuple[By, str], timeout: int = 10) -> object:
        """
        Ждет появления элемента на странице в течение указанного таймаута.

        :param locator: Кортеж локатора (например, (By.ID, "example_id")).
        :param timeout: Таймаут ожидания элемента в секундах.
        :return: Веб-элемент, если он появился.
        """
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located(locator)
        )
