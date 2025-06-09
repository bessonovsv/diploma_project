# test_data для API

TEST_DATA_1 = {
    "place_slug": "magnit_dv7qk",
    "product_public_id": "fb488f3a-7943-4fe8-8e40-9a4946d82cf2",
    "with_categories": True,
    "location": {
        "latitude": 58.50861,
        "longitude": 31.22887
    }
}

TEST_DATA_2 = {
    "item_id": "fb488f3a-7943-4fe8-8e40-9a4946d82cf2",
    "quantity": 1,
    "place_slug": "magnit_dv7qk",
    "place_business": "shop"
}

TEST_DATA_4 = {
    "text": "морковь по корейски",
    "filters": [],
    "location": {
        "longitude": 31.22887,
        "latitude": 58.50861
    }
}

TEST_DATA_5 = {
    "text": "морковь по корейски неклассическая",
    "filters": [],
    "location": {
        "longitude": 31.22887,
        "latitude": 58.50861
    }
}

# test_data для UI

TEST_DATA = {
    "shop_url": "https://market-delivery.yandex.ru/retail/magnit_celevaya?placeSlug=magnit_dv7qk",
    "product_url_fragment": "fb488f3a-7943-4fe8-8e40-9a4946d82cf2",
    "product_name_keyword": "Жевательная резинка",
    "shop_selector": 'a[aria-label*="Магнит"]',
    "confirm_button_selector": 'button.r1jyb6b1.s1v4x2t8.v102ekr4.syv67cr.b1fpzidc',
    "shop_link_selector": 'a[href*="magnit_dv7qk"]',
    "product_link_selector": 'a[href*="fb488f3a-7943-4fe8-8e40-9a4946d82cf2"]',
    "product_name_selector": 'h1[data-testid="product-full-card-name"]'
}

