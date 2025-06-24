"""
Базовый класс для реализации паттерна Page Object в Selenium-тестах.

Класс обеспечивает возможность постепенного заполнения полей формы,
эмулируя поведение реального пользователя, а также простое взаимодействие
с элементами страницы, такими как кнопки.

Используемые импорты:
- `By`: Модуль для задания способа поиска элементов на странице
(например, CSS-селектора).
- `Keys`: Набор специальных клавиш для отправки симулированных нажатий клавиш.

Атрибуты класса:
- `browser`: Объект WebDriver, используемый для взаимодействия с браузером.

Методы класса:
- `slow_fill_input_field(locator, value)`:
   Плавная отправка значений в поле ввода, постепенно заполняя каждое значение.

- `click_on_the_button(selector)`:
   Простое нажатие на кнопку по заданному CSS-селектору.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class PageObject:
    def __init__(self, browser) -> None:
        """
        Конструктор базового класса Page Object.

        :param browser: Экземпляр драйвера браузера.
        """
        self.browser = browser

    def slow_fill_input_field(self, locator: str, value: str) -> None:
        """
        Постепенный ввод текста в поле, имитируя человеческое поведение.

        :param locator: Селектор поля ввода (CSS-селектор).
        :param value: Значение, которое нужно ввести в поле.
        """
        input_field = self.browser.find_element(By.CSS_SELECTOR, locator)
        for char in value:
            input_field.send_keys(char + Keys.NULL)

    def click_on_the_button(self, selector: str) -> None:
        """
        Нажатие на кнопку по указанному селектору.

        :param selector: Селектор кнопки (CSS-селектор).
        """
        btn = self.browser.find_element(By.CSS_SELECTOR, selector)
        btn.click()
