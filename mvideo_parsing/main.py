import requests
import json

import requests as requests


def get_data():
    cookies = {
        '__lhash_': '48ec1af819e06cf6055ad5a05b0daa2e',
        'CACHE_INDICATOR': 'false',
        'COMPARISON_INDICATOR': 'false',
        'HINTS_FIO_COOKIE_NAME': '2',
        'MVID_AB_SERVICES_DESCRIPTION': 'var2',
        'MVID_ADDRESS_COMMENT_AB_TEST': '2',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'false',
        'MVID_CART_AVAILABILITY': 'true',
        'MVID_CART_MULTI_DELETE': 'false',
        'MVID_CATALOG_STATE': '1',
        'MVID_CHECKOUT_REGISTRATION_AB_TEST': '2',
        'MVID_CITY_ID': 'CityCZ_2128',
        'MVID_CREDIT_AVAILABILITY': 'true',
        'MVID_EXP_NEW_RANKING': 'true',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'MVID_GIFT_KIT': 'true',
        'MVID_GUEST_ID': '21410934612',
        'MVID_HANDOVER_SUMMARY': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '2300000100000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '2',
        'MVID_MCLICK': 'true',
        'MVID_MINDBOX_DYNAMICALLY': 'true',
        'MVID_MINI_PDP': 'true',
        'MVID_MOBILE_FILTERS': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_DESKTOP_FILTERS': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_REGION_ID': '11',
        'MVID_REGION_SHOP': 'S911',
        'MVID_SERVICES': '111',
        'MVID_SERVICES_MINI_BLOCK': 'var2',
        'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'new',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_WEBP_ENABLED': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'true',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        'flacktory': 'no',
        'searchType2': '3',
        '__hash_': 'ffc224bd6d14d37f51f255f456bf32fc',
        'MVID_SMART_BANNER_BOTTOM': 'true',
        '_gid': 'GA1.2.1005173831.1662646839',
        '_dc_gtm_UA-1873769-1': '1',
        '_sp_ses.d61c': '*',
        '_ym_uid': '1662646839508743430',
        '_ym_d': '1662646839',
        '_ym_isad': '1',
        '__SourceTracker': 'google__organic',
        'admitad_deduplication_cookie': 'google__organic',
        'SMSError': '',
        'authError': '',
        '_dc_gtm_UA-1873769-37': '1',
        'tmr_lvid': 'ba31af2bf686c6159a183681209b48ef',
        'tmr_lvidTS': '1662646843986',
        'advcake_track_id': 'eac11109-5a62-2cf9-30a4-ef6665d27bc3',
        'advcake_session_id': 'a95d7138-af86-b7ad-1c4f-eced297deae5',
        'uxs_uid': '6cd52cb0-2f81-11ed-a6c6-45ef828ae8a5',
        'st_uid': '88d527b5c99fc039599b7ff38b945096',
        'flocktory-uuid': '872756a2-f1b7-46cc-94e6-cf002ba6bd3b-0',
        'afUserId': '1cea560a-4eb0-444b-996c-8b736f598af8-p',
        'AF_SYNC': '1662646844948',
        'BIGipServeratg-ps-prod_tcp80': '2466569226.20480.0000',
        'bIPs': '-314595793',
        'JSESSIONID': 'mV6YjZ6QGm7pTgJT21C8c7wrXhnnXTsKnTp6pTgxRwq26hv8WLpr!-393784284',
        '_sp_id.d61c': '0e555910-befb-40f1-9390-fa9662ac7004.1662646839.1.1662646851..68896561-df5c-406a-8958-7b22092e731e..f207f85e-ba99-42d1-aeb8-21f8aeede578.1662646838917.2',
        '_ga': 'GA1.2.136057538.1662646839',
        'tmr_detect': '1%7C1662646857473',
        'tmr_reqNum': '20',
        '_ga_CFMZTSS5FM': 'GS1.1.1662646839.1.1.1662646860.0.0.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1662646838.1.1.1662646860.38.0.0',
        'MVID_ENVCLOUD': 'prod2',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'baggage': 'sentry-transaction=%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=34e1f6eac3164ebba46d165ec7d01bf3,sentry-sample_rate=0%2C5',
        # Requests sorts cookies= alphabetically
        # 'cookie': '__lhash_=48ec1af819e06cf6055ad5a05b0daa2e; CACHE_INDICATOR=false; COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=2; MVID_AB_SERVICES_DESCRIPTION=var2; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=false; MVID_CART_AVAILABILITY=true; MVID_CART_MULTI_DELETE=false; MVID_CATALOG_STATE=1; MVID_CHECKOUT_REGISTRATION_AB_TEST=2; MVID_CITY_ID=CityCZ_2128; MVID_CREDIT_AVAILABILITY=true; MVID_EXP_NEW_RANKING=true; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GUEST_ID=21410934612; MVID_HANDOVER_SUMMARY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=2300000100000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=2; MVID_MCLICK=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_MOBILE_FILTERS=true; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=11; MVID_REGION_SHOP=S911; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_TAXI_DELIVERY_INTERVALS_VIEW=new; MVID_TIMEZONE_OFFSET=3; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PRESELECT_COURIER_DELIVERY_FOR_KBT=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; flacktory=no; searchType2=3; __hash_=ffc224bd6d14d37f51f255f456bf32fc; MVID_SMART_BANNER_BOTTOM=true; _gid=GA1.2.1005173831.1662646839; _dc_gtm_UA-1873769-1=1; _sp_ses.d61c=*; _ym_uid=1662646839508743430; _ym_d=1662646839; _ym_isad=1; __SourceTracker=google__organic; admitad_deduplication_cookie=google__organic; SMSError=; authError=; _dc_gtm_UA-1873769-37=1; tmr_lvid=ba31af2bf686c6159a183681209b48ef; tmr_lvidTS=1662646843986; advcake_track_id=eac11109-5a62-2cf9-30a4-ef6665d27bc3; advcake_session_id=a95d7138-af86-b7ad-1c4f-eced297deae5; uxs_uid=6cd52cb0-2f81-11ed-a6c6-45ef828ae8a5; st_uid=88d527b5c99fc039599b7ff38b945096; flocktory-uuid=872756a2-f1b7-46cc-94e6-cf002ba6bd3b-0; afUserId=1cea560a-4eb0-444b-996c-8b736f598af8-p; AF_SYNC=1662646844948; BIGipServeratg-ps-prod_tcp80=2466569226.20480.0000; bIPs=-314595793; JSESSIONID=mV6YjZ6QGm7pTgJT21C8c7wrXhnnXTsKnTp6pTgxRwq26hv8WLpr!-393784284; _sp_id.d61c=0e555910-befb-40f1-9390-fa9662ac7004.1662646839.1.1662646851..68896561-df5c-406a-8958-7b22092e731e..f207f85e-ba99-42d1-aeb8-21f8aeede578.1662646838917.2; _ga=GA1.2.136057538.1662646839; tmr_detect=1%7C1662646857473; tmr_reqNum=20; _ga_CFMZTSS5FM=GS1.1.1662646839.1.1.1662646860.0.0.0; _ga_BNX5WPP3YK=GS1.1.1662646838.1.1.1662646860.38.0.0; MVID_ENVCLOUD=prod2',
        'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/planshety-195?from=homepage',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': '34e1f6eac3164ebba46d165ec7d01bf3-a7c3ece38eb0bcec-0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'x-set-application-id': '30901187-260a-4627-8e3f-465995d22196',
    }

    params = {
        'categoryId': '195',
        'offset': '0',
        'limit': '24',
        'doTranslit': 'true',
    }
    # получил все данные о товарах
    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                            headers=headers).json()
    # собрал айдишники товаров
    products_ids = response.get('body').get('products')

    with open('1_products_ids.json', 'w') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)

    json_data = {
        'productIds': products_ids,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }
    #получил данные о планшетах
    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
                             json=json_data).json()

    with open('2_items.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    products_ids_str = ','.join(products_ids)

    params = {
        'productIds': products_ids_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }
    # собрал цены,скидки и бонусы на планшеты
    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,
                            headers=headers).json()

    with open("3_prices.json", 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    items_prices = {}
    material_prices = response.get('body').get('materialPrices')
    for item in material_prices:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_sale_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')
        items_prices[item_id] = {
            'item_basePrice': item_base_price,
            'item_salePrice': item_sale_price,
            'item_bonus': item_bonus
        }
    with open('4_items_prices.json', 'w') as file:
        json.dump(items_prices, file, indent=4, ensure_ascii=False)


def get_result():
    with open('2_items.json', 'r') as file:
        products_data = json.load(file)
    with open('4_items_prices.json.json', 'r') as file:
        products_prices = json.load(file)
    products_data = products_data.get('body').get('products')
    for item in products_prices:
        product_id = item.get('productId')
        if product_id in products_prices:
            prices = products_prices[product_id]
        item['item_basePrice'] = prices.get('item_basePrice')
        item['item_salePrice'] = prices.get('item_salePrice')
        item['item_bonus'] = prices.get('item_bonus')
    with open('5_result', 'w'):
        json.dump(products_data, file, indent=4, ensure_ascii=False)


def main():
    get_data()
    get_result()


if __name__ == "__main__":
    main()
