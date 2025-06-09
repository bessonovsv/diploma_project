import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from typing import Tuple
from .page_object import PageObject


class MainPage(PageObject):
    def __init__(self, browser) -> None:
        """
        Конструктор класса MainPage.

        :param browser: объект браузера Selenium
        """
        super().__init__(browser)

    @allure.step("Открыть страницу по URL: {url}")
    def open(self, url: str) -> None:
        """
        Открывает заданный URL в браузере.

        :param url: строка с адресом страницы
        """
        self.browser.get(url)

    @allure.step("Нажать на кнопку")
    def click_on_the_button(self, selector: str) -> None:
        """
        Нажимает кнопку по указанному селектору.

        :param selector: CSS-селектор кнопки
        """
        try:
            wait = WebDriverWait(self.browser, 30)
            button = wait.until(EC.element_to_be_clickable
                                ((By.CSS_SELECTOR, selector)))
            button.click()
            print(f"[LOG] Клик выполнен по кнопке с селектором: {selector}")
        except Exception as e:
            print(f"Ошибка при нажатии на кнопку: {e}")
            raise RuntimeError(f"Кнопка с селектором '{selector}' "
                               f"не найдена или недоступна")

    @allure.step("Проверить содержание текста")
    def text_verification(self, selector: str) -> str:
        """
        Получает текст элемента по указанному селектору.

        :param selector: CSS-селектор элемента
        :return: текст элемента
        """
        wait = WebDriverWait(self.browser, 10)
        element = wait.until(EC.presence_of_element_located
                             ((By.CSS_SELECTOR, selector)))
        return element.text

    @allure.step("Проверка наличия элемента")
    def checking_the_element(self, selector: str) -> bool:
        """
        Проверяет наличие элемента по указанному селектору.

        :param selector: CSS-селектор элемента
        :return: True, если элемент присутствует, иначе False
        """
        try:
            wait = WebDriverWait(self.browser, 30)
            element = wait.until(EC.presence_of_element_located
                                 ((By.CSS_SELECTOR, selector)))
            print(f"[LOG] Элемент найден: {selector}")
            return bool(element)
        except Exception as e:
            print(f"Ошибка при проверке элемента: {e}")
            raise RuntimeError(f"Элемент с селектором '{selector}' не найден")

    @allure.step("Ввести текст '{value}' в поле с селектором {selector}")
    def fill_input_field(self, selector: str, value: str) -> None:
        """
        Вводит текст в текстовое поле.

        :param selector: CSS-селектор поля ввода
        :param value: текст для ввода
        """
        wait = WebDriverWait(self.browser, 10)
        input_field = wait.until(EC.visibility_of_element_located
                                 ((By.CSS_SELECTOR, selector)))
        input_field.clear()  # Очистка поля перед вводом
        input_field.send_keys(value)  # Ввод значения

    @allure.step("Медленный ввод текста '{value}' "
                 "в поле с селектором {locator}")
    def slow_fill_input_field(self, locator: str, value: str) -> None:
        """
        Пошагово вводит текст в поле, имитируя человеческое поведение.

        :param locator: CSS-селектор поля ввода
        :param value: текст для ввода
        """
        input_field = self.browser.find_element(By.CSS_SELECTOR, locator)
        for char in value:
            input_field.send_keys(char + Keys.NULL)

    @allure.step("Прокрутить страницу медленно до элемента")
    def scroll_to_element_slowly(self, by_locator: Tuple[str, str],
                                 max_attempts: int = 20,
                                 step: int = 150) -> object:
        """
        Медленная прокрутка страницы вниз до появления нужного элемента.

        :param by_locator: локатор элемента
        :param max_attempts: максимальное число попыток прокрутки
        :param step: размер шага прокрутки в пикселях
        :raises: Exception, если элемент не найден после всех попыток
        """
        for _ in range(max_attempts):
            try:
                element = WebDriverWait(self.browser, 2).until(
                    EC.visibility_of_element_located(by_locator)
                )
                if element.is_displayed() and element.is_enabled():
                    return element
            except:
                pass

            # Прокрутка вниз на небольшое количество пикселей
            self.browser.execute_script(f"window.scrollBy(0,{step});")
            # Пауза между попытками
            WebDriverWait(self.browser, 0.5).until(lambda driver: True)

        raise Exception(f"Элемент не найден после {max_attempts} "
                        f"попыток прокрутки: {by_locator}")

    @allure.step("Кликнуть на видимый элемент плавно")
    def click_on_visible_element_slowly(self, element_id: str) -> None:
        """
        Выполняет плавный клик по видимому элементу.

        :param element_id: идентификатор элемента (CSS-селектор)
        """
        by_locator = (By.CSS_SELECTOR, element_id)
        element = self.scroll_to_element_slowly(by_locator)
        # Ждем пока элемент станет кликабельным
        (WebDriverWait(self.browser, 10)
         .until(EC.element_to_be_clickable(by_locator)))
        element.click()
