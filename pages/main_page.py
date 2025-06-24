"""
Модуль main_page.py

Данный модуль реализует основной класс страницы (`MainPage`),
предназначенный для управления основными операциями взаимодействия
с элементами веб-интерфейса.
Класс наследует функциональность базового класса `PageObject`,
предоставляя дополнительные удобства для действий,
таких как открытие страницы, выполнение кликов и ввод текста в поля формы.

Основные возможности класса включают:
- Открытие конкретной страницы по URL.
- Ожидание полной загрузки страницы.
- Нажатие кнопок по CSS-селекторам.
- Получение текста элементов.
- Медленное заполнение полей ввода, имитирующее человеческие действия.
- Прокрутку страницы до конкретного элемента.
- Плавный клик по видимому элементу.

Использование Allure Reporting позволяет детально отслеживать
шаги каждого теста, что повышает прозрачность и
удобство отслеживания результатов тестов.

Класс активно взаимодействует с объектами Selenium и
поддерживает различные условия ожидания,
обеспечивая надежность тестируемых сценариев.

Импортируемые модули:

- By: модуль для выбора элементов на веб-странице
различными методами (id, class_name, xpath и прочими селекторами).
- WebDriverWait: класс для организации ожиданий появления нужного
элемента на странице перед выполнением дальнейших операций.
- EC (expected_conditions): библиотека предопределённых условий для
ожидания изменений в состоянии страницы
(например, появление элемента, кликабельность и т.п.).
- TimeoutException: исключение, которое возникает, если элемент
не появился на странице в заданный лимит времени.
- WebElement: класс, представляющий найденные элементы HTML-документа,
позволяющие взаимодействовать с ними (например, кликнуть или ввести текст).
- Keys: специальный модуль, предоставляющий константы клавиш клавиатуры
для эмуляции нажатий (например, Enter, Tab, Shift).
- Tuple: стандартный тип данных для обозначения кортежей — неизменяемых
последовательностей объектов. Используется для аннотаций типов.
- Allure: библиотека для интеграции Allure Reporting Framework,
позволяющая создавать отчёты о тестировании и фиксировать
шаги выполнения тестов.
"""

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from typing import Tuple
from .page_object import PageObject


class MainPage(PageObject):
    """
    Основной класс страницы, реализующий базовые операции
    над элементами интерфейса сайта.
    Наследуется от базового класса PageObject.
    Предоставляет удобные методы для открытия страницы,
    кликов, ввода текста и проверок.
    """

    def __init__(self, browser) -> None:
        """
        Конструктор класса MainPage.

        :param browser: Объект браузера Selenium.
        """
        super().__init__(browser)

    @allure.step("Открыть страницу по URL: {url}")
    def open(self, url: str) -> None:
        """
        Открывает заданный URL в браузере.

        :param url: Строка с адресом страницы.
        """
        self.browser.get(url)

    @allure.step("Ожидание полной загрузки страницы")
    def wait_until_loaded(self, timeout=30):
        """
        Ожидает полной загрузки страницы.

        :param timeout: Время ожидания в секундах.
        """
        wait = WebDriverWait(self.browser, timeout)
        wait.until(
            lambda driver: driver.execute_script("return document.readyState")
            == "complete"
        )

    @allure.step("Нажать на кнопку")
    def click_on_the_button(self, selector: str) -> None:
        """
        Нажимает кнопку по указанному селектору.

        :param selector: CSS-селектор кнопки.
        """
        try:
            wait = WebDriverWait(self.browser, 30)
            button = wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, selector)))
            button.click()
        except Exception as e:
            print(f"Ошибка при нажатии на кнопку: {e}")
            raise RuntimeError(
                f"Кнопка с селектором '{selector}' не найдена или недоступна"
            )

    @allure.step("Получить текст элемента")
    def text_verification(self, selector: str) -> str:
        """
        Возвращает текст элемента по указанному селектору.

        :param selector: CSS-селектор элемента.
        :return: Текст элемента.
        """
        wait = WebDriverWait(self.browser, 10)
        element = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        )
        return element.text

    @allure.step("Проверить наличие элемента")
    def checking_the_element(self, selector: str) -> bool:
        """
        Проверяет наличие элемента по указанному селектору.

        :param selector: CSS-селектор элемента.
        :return: True, если элемент присутствует, иначе False.
        """
        try:
            wait = WebDriverWait(self.browser, 30)
            element = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selector))
            )
            return bool(element)
        except Exception as e:
            print(f"Ошибка при проверке элемента: {e}")
            raise RuntimeError(f"Элемент с селектором '{selector}' не найден")

    @allure.step(
        "Медленный ввод текста '{value}' в поле с селектором {locator}")
    def slow_fill_input_field(self, locator: str, value: str) -> None:
        """
        Поэтапно вводит текст в поле, имитируя человеческое поведение.

        :param locator: CSS-селектор поля ввода.
        :param value: Текст для ввода.
        """
        input_field = self.browser.find_element(By.CSS_SELECTOR, locator)
        for char in value:
            input_field.send_keys(char + Keys.NULL)

    @allure.step("Прокручивает страницу медленно до элемента")
    def scroll_to_element_slowly(
        self, by_locator: Tuple[str, str], max_attempts: int = 20,
            step: int = 150
    ) -> WebElement:
        """
        Осуществляет медленную прокрутку страницы вниз до
        появления нужного элемента.

        :param by_locator: Локатор элемента (кортеж вида
        (метод_локатора, значение)).
        :param max_attempts: Максимальное число попыток
        прокрутки (по умолчанию 20).
        :param step: Размер шага прокрутки в пикселях
        (по умолчанию 150 пикселей).
        :returns: Найденный элемент (WebElement).
        :raises: Param Exception, если элемент не найден после всех попыток.
        """
        for _ in range(max_attempts):
            try:
                element = WebDriverWait(self.browser, 2).until(
                    EC.visibility_of_element_located(by_locator)
                )
                if element.is_displayed() and element.is_enabled():
                    return element
            except TimeoutException:
                # Если элемент не найден, прокручиваем страницу вниз
                self.browser.execute_script(f"window.scrollBy(0, {step});")

        raise Exception(
            f"Элемент не найден после {max_attempts} "
            f"попыток прокрутки: {by_locator}"
        )

    @allure.step("Выполнить плавный клик по видимому элементу")
    def click_on_visible_element_slowly(self, element_id: str) -> None:
        """
        Выполняет плавный клик по указанному элементу.

        :param element_id: Идентификатор элемента (CSS-селектор).
        """
        by_locator = (By.CSS_SELECTOR, element_id)
        element = self.scroll_to_element_slowly(by_locator)
        # Ждем пока элемент станет кликабельным
        WebDriverWait(
            self.browser, 30).until(
            EC.element_to_be_clickable(element))
        element.click()
