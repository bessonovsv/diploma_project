"""
Тестовый сценарий для UI-тестирования главной страницы приложения.

Цель: Автоматизированное тестирование взаимодействия пользователя с интерфейсом
главной страницы веб-приложения с использованием Selenium и Pytest.

Особенности:
- Используется библиотека Selenium для автоматизации действий браузера.
- Применяются ожидаемые условия (Expected Conditions)
для проверки состояния DOM-элементов.
- Реализованы механизмы ожидания загрузки элементов на странице.
- Обрабатываются исключения, возникающие при взаимодействии
с элементами страницы.

Ключевые компоненты:
- Модули allure и pytest обеспечивают организацию и отчетность тестов.
- Экземпляр страницы (MainPage) служит основным объектом
для навигации и взаимодействий.
- Константы из файла settings содержат селекторы и значения,
используемые в тестах.
"""

import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import (TimeoutException,
                                        StaleElementReferenceException)


from pages.main_page import MainPage
from settings import SELECTORS, VALUE, UI_URL


@pytest.mark.ui
@allure.title("Переход на страницу товара в магазине-партнёре")
def test_product_in_the_partner_store(browser):
    wait = WebDriverWait(browser, 30)

    with allure.step("Открываем главную страницу"):
        page = MainPage(browser)
        page.open(UI_URL)
        print("[TEST LOG] Главная страница открыта")

    with allure.step("Переходим к магазину-партнёру"):
        page.click_on_the_button(SELECTORS["shop_link"])
        print("[TEST LOG] Перешли в магазин партнёра")

    with allure.step("Проверяем что перешли на страницу магазина"):
        assert page.checking_the_element(
            SELECTORS["unique_element"]
        ), "Не удалось найти уникальный элемент на странице магазина"
        print("[TEST LOG] Успешно нашли уникальный элемент магазина")

    with allure.step("Добавляем товар в корзину"):
        page.click_on_the_button(SELECTORS["product_button"])
        print("[TEST LOG] Товары добавлены в корзину")

    with allure.step("Проверяем наличие названия товара"
                     " и выводим его в отчет"):
        product_name_element = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, SELECTORS["product_name"])
            )
        )
        product_name = product_name_element.text.strip()
        print(f"[TEST LOG] Название товара получено: {product_name}")

        # Assert: проверяем, что элемент с названием товара найден и не пуст
    with allure.step("Проверяем наличие названия товара"):
        assert len(product_name) > 0, "Название товара не найдено или пустое"


@pytest.mark.ui
@allure.title("Поиск товаров в поисковой строке")
def test_search_morkov_po_koreyski(browser):
    with allure.step("Открываем главную страницу"):
        page = MainPage(browser)
        page.open(UI_URL)
        print("[TEST LOG] Главная страница открыта")

    with allure.step("Ожидаем полной загрузки страницы"):
        page.wait_until_loaded()
        print("[TEST LOG] Страница полностью загружена")

    with allure.step("Проверяем доступность поля поиска перед вводом"):
        wait = WebDriverWait(browser, 30)
        try:
            search_field = wait.until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, SELECTORS["product_search"])
                )
            )
            if not search_field.is_displayed():
                print("[WARNING] Поле поиска не отображается!")
        except NoSuchElementException:
            print("[ERROR] Селектор не найден:", SELECTORS["product_search"])
            print("\nHTML-код страницы на момент ошибки:")
            print(browser.page_source)

    with allure.step("Вводим в поле поиска текст"):
        page.slow_fill_input_field(
            SELECTORS["product_search"],
            VALUE["product"])
        print("[TEST LOG] Текст введён")

    with allure.step("Нажимаем кнопку Найти"):
        page.click_on_the_button(SELECTORS["the_find_button"])
        print("[TEST LOG] Кнопка найти нажата")

    with allure.step("Ждем появление результата поиска"):
        wait = WebDriverWait(page.browser, 60)
        try:
            element = wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, SELECTORS["response_text"])
                )
            )
            wait.until(EC.visibility_of(element))
        except TimeoutException:
            print(
                "[ERROR] Время ожидания истекло! Текущий HTML-код"
                " страницы:\n\n{browser.page_source}"
            )
            raise Exception("Результат поиска не обнаружен.")

    with allure.step("Проверяем наличие товара"):
        response = page.text_verification(SELECTORS["response_text"])
        assert response.startswith(SELECTORS["expected_text"]), (
            f"Ошибка: Ответ '{response}' не начинается с "
            f"'{SELECTORS['expected_text']}': {response}"
        )
        print(f"Текст ответа: {response}")


@pytest.mark.ui
@allure.title("Ввод в поисковую строку невалидного текста")
def test_search_invalid_value(browser):
    with allure.step("Открываем главную страницу"):
        page = MainPage(browser)
        page.open(UI_URL)
        print("[TEST LOG] Главная страница открыта")

    with allure.step("Ожидаем полной загрузки страницы"):
        page.wait_until_loaded()
        print("[TEST LOG] Страница полностью загружена")

    with allure.step("Проверяем доступность поля поиска перед вводом"):
        wait = WebDriverWait(browser, 30)
        try:
            search_field = wait.until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, SELECTORS["product_search"])
                )
            )
            if not search_field.is_displayed():
                print("[WARNING] Поле поиска не отображается!")
        except TimeoutException:
            print(
                f"[ERROR] Элемент не появился вовремя ("
                f"{SELECTORS['product_search']})")
        except StaleElementReferenceException:
            print(
                f"[ERROR] Страница обновилась, элемент устарел ("
                f"{SELECTORS['product_search']})")
        except Exception as e:
            print(f"[CRITICAL ERROR]: {type(e).__name__}: {e}")
            print("\nHTML-код страницы на момент ошибки:")
            print(browser.page_source)

    with allure.step("Вводим в поле поиска текст"):
        page.slow_fill_input_field(
            SELECTORS["product_search"],
            VALUE["invalid_value"])
        print("[TEST LOG] Текст введён")

    with allure.step("Нажимаем кнопку Найти"):
        page.click_on_the_button(SELECTORS["the_find_button"])
        print("[TEST LOG] Кнопка найти нажата")

    with allure.step("Ждем появление результата поиска"):
        wait = WebDriverWait(page.browser, 60)
        try:
            element = wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, SELECTORS["response_text"])
                )
            )
            wait.until(EC.visibility_of(element))
        except TimeoutException:
            print(
                "[ERROR] Время ожидания истекло! Текущий HTML-код"
                " страницы:\n\n{browser.page_source}"
            )
            raise Exception("Результат поиска не обнаружен.")

    with allure.step("Проверяем наличие товара"):
        response = page.text_verification(SELECTORS["response_text"])
        assert response.startswith(SELECTORS["expected_text_1"]), (
            f"Ошибка: Ответ '{response}' не начинается с "
            f"'{SELECTORS['expected_text_1']}': {response}"
        )
        print(f"Текст ответа: {response}")


@pytest.mark.ui
@allure.title("Выбор адреса доставки")
def test_select_delivery_address(browser):
    """Тест проверки возможности выбрать адрес доставки."""
    with allure.step("Открываем главную страницу"):
        page = MainPage(browser)
        page.open(UI_URL)
        print("[TEST LOG] Главная страница открыта")

    with allure.step("Ожидаем полной загрузки страницы"):
        page.wait_until_loaded()
        print("[TEST LOG] Страница полностью загружена")

    with allure.step("Нажимаем кнопку Укажите адрес доставки"):
        page.click_on_the_button(SELECTORS["address_button"])
        print("[TEST LOG] Кнопка Укажите адрес доставки нажата")

    with allure.step("Ожидаем появления поля для ввода адреса"):
        wait = WebDriverWait(browser, 30)
        input_field = wait.until(
            EC.visibility_of_element_located(SELECTORS["address_field"])
        )
        print("[TEST LOG] Поле для ввода адреса найдено")

    with allure.step("Заполняем поле адресом"):
        input_field.clear()
        input_field.send_keys(VALUE["address"])
        print("[TEST LOG] Адрес введен")

    with allure.step("Проверяем соответствие введённого адреса заявленному"):
        current_value = input_field.get_attribute("value")
        assert current_value == VALUE["address"], (
            f"Фактический адрес '{current_value}' "
            f"не совпадает с ожидаемым '{VALUE['address']}'"
        )
        print("[TEST LOG] Введённый адрес корректен")


@pytest.mark.ui
@allure.title("Выбор еды в разделе ресторанов")
def test_food_in_restaurants(browser):
    with allure.step("Открываем главную страницу"):
        page = MainPage(browser)
        page.open(UI_URL)
        print("[TEST LOG] Главная страница открыта")

    with allure.step("Ожидаем полной загрузки страницы"):
        page.wait_until_loaded()
        print("[TEST LOG] Страница полностью загружена")

    with allure.step("Нажимаем кнопку Ещё в разделе Рестораны"):
        page.click_on_visible_element_slowly(SELECTORS["the_more_button"])
        print("[TEST LOG] Открылся раздел с едой")

    with allure.step("Ожидаем полной загрузки страницы"):
        page.wait_until_loaded()
        print("[TEST LOG] Страница полностью загружена")

    with allure.step("В выпадающем списке выбираем раздел еды"):
        page.click_on_visible_element_slowly(SELECTORS["the_baking_button"])
        print("[TEST LOG] Раздел с едой выбран")

    with allure.step("Ожидаем полной загрузки страницы"):
        page.wait_until_loaded()
        print("[TEST LOG] Страница полностью загружена")

    with allure.step("Переходим в кафе"):
        page.click_on_visible_element_slowly(SELECTORS["cafe_button"])
        print("[TEST LOG] Переход в кафе осуществлён")

    with allure.step("Ожидаем полной загрузки страницы"):
        page.wait_until_loaded()
        print("[TEST LOG] Страница полностью загружена")

    with allure.step("Выбираем еду"):
        page.click_on_visible_element_slowly(SELECTORS["food_selection"])
        print("[TEST LOG] Еда выбрана")

    with allure.step("Ожидаем появления поля для ввода адреса"):
        wait = WebDriverWait(browser, 30)
        address_input_field = wait.until(
            EC.visibility_of_element_located(SELECTORS["address_field"])
        )
        print("[TEST LOG] Поле для ввода адреса найдено")

        with allure.step("Проверяем доступность поля для ввода адреса"):
            assert address_input_field.is_displayed() is True, (
                "Поле для ввода " "адреса не отображается на странице."
            )
