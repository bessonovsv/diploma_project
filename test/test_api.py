import allure
import pytest
from settings import (BASE_URL, API_URL, ENDPOINT_1, ENDPOINT_2,
                      ENDPOINT_3, ENDPOINT_4, ENDPOINT_5)
from test_data import TEST_DATA_1, TEST_DATA_2, TEST_DATA_4, TEST_DATA_5
from test.conftest import session


@allure.title("Выбор товара в магазине Магнит")
@pytest.mark.api
def test_select_product_magnet(session):
    url = f"{API_URL}{ENDPOINT_1}"
    with allure.step("Отправляем POST-запрос к API"):
        response = session.post(url, json=TEST_DATA_1)

    with allure.step("Проверяем статус-код ответа"):
        assert response.status_code == 200, ("Expected status 200, "
                                             "got {response.status_code}")

    with allure.step("Проверяем наличие текста "
                     "'Жевательная резинка' в ответе"):
        assert "Жевательная резинка" in response.text, ("Ответ не содержит "
                                                        "ожидаемый товар")


@allure.title("Добавление товара в корзину в магазине Магнит")
@pytest.mark.api
def test_add_product_to_cart_magnet(session):
    url = f"{API_URL}{ENDPOINT_2}"
    with allure.step("Отправляем POST-запрос к API"):
        response = session.post(url, json=TEST_DATA_2)

    with allure.step("Проверяем статус-код ответа"):
        assert response.status_code == 200, ("Expected status 200, "
                                             "got {response.status_code}")

    with allure.step("Проверка наличия текста 'Жевательная резинка' в ответе"):
        assert "Жевательная резинка" in response.text, ("Текст 'Жевательная резинка' "
                                                        "не найден в ответе")


@allure.title("Удаление товара из корзины в магазине Магнит")
@pytest.mark.api
def test_delete_product_from_cart_magnet(session):
    url = f"{API_URL}{ENDPOINT_3}"
    with allure.step("Отправляем DELETE-запрос к API"):
        response = session.delete(url)

    with allure.step("Проверяем статус-код ответа"):
        assert response.status_code == 204, ("Expected status 204,"
                                             " got {response.status_code}")


@allure.title("Поиск товара 'Морковь по корейски' на сайте")
@pytest.mark.api
def test_search_product_by_text(session):
    url = f"{BASE_URL}{ENDPOINT_4}"
    with allure.step("Отправляем POST-запрос к API"):
        response = session.post(url, json=TEST_DATA_4)

    with allure.step("Проверка статус-кода ответа"):
        assert response.status_code == 200, ("Expected status code 200, "
                                             "got {response.status_code}")

    with allure.step("Проверка наличия текста 'Морковь по корейски' в ответе"):
        assert "Морковь по корейски" in response.text, ("Текст 'Морковь по корейски' не "
                                                        "найден в ответе")


@allure.title("Поиск несуществующего товара 'морковь по корейски неклассическая'")
@pytest.mark.api
def test_search_nonexistent_product(session):
    url = f"{BASE_URL}{ENDPOINT_5}"
    with allure.step("Отправляем POST-запрос к API"):
        response = session.post(url, json=TEST_DATA_5)

    with allure.step("Проверка статус-кода ответа"):
        assert response.status_code == 200, ("Expected status code 200, "
                                             "got {response.status_code}")

    with allure.step("Проверка наличия фразы 'не нашли' в ответе"):
        assert "не нашли" in response.text, ("Фраза 'не нашли' "
                                             "не найдена в ответе")
