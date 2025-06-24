"""
Модуль конфигурации для автотестирования сервиса Яндекс.Маркет Доставка.

Данный файл содержит необходимые константы и переменные
для инициализации тестов:
- Параметры для импорта селекторов элементов страницы (By).
- Базовые URL-адреса для тестирования API и веб-интерфейса.
- Константы с конечными точками API (endpoints), заголовками
HTTP-запросов и cookies.
- Тестовые значения для адреса, наименования продукта
и недействительных значений.
- Набор CSS-селекторов для автоматического взаимодействия с элементами страниц.

Использование модуля позволяет легко настраивать тесты и упрощает
процесс разработки новых сценариев.
"""

# Импорт классов для задания способов нахождения элементов (By)
from selenium.webdriver.common.by import By

# Настройки URL
BASE_URL = "https://market-delivery.yandex.ru"
API_URL = "https://market-delivery.yandex.ru/api/"
UI_URL = "https://market-delivery.yandex.ru/Velikiy-Novgorod?shippingType=delivery"
MAGNIT_URL = (
    "https://market-delivery.yandex.ru/retail/magnit_celevaya?"
    + "placeSlug=magnit_dv7qk"
)
PURCHASE_1_URL = (
    "https://market-delivery.yandex.ru/retail/magnit_celevaya?"
    "item=fb488f3a-7943-4fe8-8e40-9a4946d82cf2&placeSlug=magnit_dv7qk"
)
PURCHASE_URL = (
    "https://market-delivery.yandex.ru/retail/magnit_celevaya?"
    "placeSlug=magnit_celevaya_bdvsq"
)

# Дополнительные настройки URL для тестов
ENDPOINT_1 = "v2/menu/product?auto_translate=false"
ENDPOINT_2 = (
    "v1/cart?longitude=31.22887&latitude=58.50861&"
    "screen=menu&shippingType=delivery&autoTranslate=false"
)
ENDPOINT_3 = (
    "v2/cart?longitude=31.22887&latitude=58.50861&"
    "screen=checkout&shippingType=delivery&autoTranslate=false"
)
ENDPOINT_4 = "/eats/v1/full-text-search/v1/search"
ENDPOINT_5 = "/eats/v1/full-text-search/v1/search"

HEADERS = {
    "Content-Type": "application/json",
}

COOKIES = {
    "_yasc": "+AEhlHp8v/Sql1fGrrzRldq6n1anUithbS769ar" "BjKH0hDG0nxxawuh4XvRPfceFbg==",
    "i": "DaqnckxTub6fN4/LhO8ZPZhGv9uauEwI4LcBwLZzVSynRrysRAPz"
    "58lpE8fjaKLHAj3S+BZGMTmJen0TZxi0cYvSNRI=",
    "yandexuid": "6611234691738403650",
    "yashr": "4974273201739964783",
    "Eats-Session": "03828fa2295c4d33b7524ad613d832ce",
}

VALUE = {
    "address": "Октябрьская ул., 1, Великий Новгород",
    "product": "Морковь по корейски",
    "invalid_value": "анелжщш9щ8делапд",
}

# Селекторы
SELECTORS = {
    "authorization_button": 'button.Avatar_avatarButton[aria-label="Профиль"]',
    "confirm_address_button": 'button[data-testid="top-bar-confirm"]',
    "shop_link": "#main > div > div > main > div:nth-child(3) > div > div > "
    "div > div > ul > li:nth-child(1) > div > a > div > div.ckb1wui",
    "unique_element": 'a[aria-label*="Магнит"]',
    "product_button": "a.f1d17p5r",
    "product_name": ".cllwzwr",
    "product_search": 'input[aria-label="Найти ресторан, блюдо или товар"]',
    "the_find_button": "button.UIInputAction_root",
    "carrot_button_in_Korean": 'button.f1d17p5r[aria-label="Морковь '
    'по-корейски 200 г, 75, 200г"]',
    "product_name_1": "h1.cllwzwr",
    "response_text": ".ptdetd8.UiKitText_root.UiKitText_Title2Loose."
    "UiKitText_Bold.UiKitText_Text",
    "expected_text": "Найдено",
    "expected_text_1": "Ничего не нашли, но есть:",
    "address_button": ".r1jyb6b1.s1v4x2t8.bmswzef.a127dc8f.b1b9rjk2",
    "address_field": (By.CSS_SELECTOR, '[data-testid="address-input"]'),
    "text_of_the_delivery_form": ".hs8s3dy",
    "the_more_button": 'span.m1xk7j8f[role="tab"]',
    "the_baking_button": ".o3ktzgh",
    "cafe_button": ".c3o0i8d",
    "food_selection": ".f1d17p5r",
}
