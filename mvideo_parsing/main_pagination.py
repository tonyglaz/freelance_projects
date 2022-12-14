import os.path
import requests
import json
from config import cookies, headers
import math
from time import sleep


def get_data():
    params = {
        'categoryId': '205',
        'offset': '0',
        'limit': '24',
        'filterParams': 'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
        'doTranslit': 'true',
    }

    if not os.path.exists('data'):
        os.mkdir('data')
    s = requests.Session()
    response = s.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                            headers=headers).json()
    total_items = response.get('body').get('total')
    if total_items is None:
        return '[!] no items [!]'
    page_count = math.ceil(total_items / 24)
    print(f'total positions: {total_items} total pages: {page_count}')
    products_ids = {}
    products_description = {}
    products_prices = {}
    for i in range(page_count):
        #sleep(3)
        offset = f'{i * 24}'
        params = {
            'categoryId': '205',
            'offset': offset,
            'limit': '24',
            'doTranslit': 'true',
        }
        response = s.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,headers=headers).json()
        products_ids_list = response.get('body').get('products')
        #print(products_ids_list)
        products_ids[i] = products_ids_list
        json_data = {
            'productIds': products_ids_list,
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
        response = s.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,json=json_data).json()
        #print(response['body'])
        products_description[i] = response
        with open(f'data/2_req/{i+1}_prod_desc.json', 'w', encoding='utf-8') as file:
            json.dump(products_description[i], file, indent=4, ensure_ascii=False)
        # print(response)
        products_ids_str = ','.join(products_ids_list)

        params = {
            'productIds': products_ids_str,
            'addBonusRubles': 'true',
            'isPromoApplied': 'true',
        }
        response = s.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,
                         headers=headers).json()
        material_prices = response.get('body').get('materialPrices')

        for item in material_prices:
            item_id = item.get('price').get('productId')
            item_base_price = item.get('price').get('basePrice')
            item_sale_price = item.get('price').get('salePrice')
            item_bonus = item.get('bonusRubles').get('total')
            products_prices[item_id] = {
                'item_basePrice': item_base_price,
                'item_salePrice': item_sale_price,
                'item_bonus': item_bonus
            }
        print(f'[+] Finished {i + 1} of the {page_count} pages')
    with open('data/1_product_ids.json', 'w') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)
    with open('data/2_product_description.json', 'w',encoding='utf-8') as file:
        json.dump(products_description, file, indent=4, ensure_ascii=False)
    with open('data/3_products_prices.json', 'w') as file:
        json.dump(products_prices, file, indent=4, ensure_ascii=False)


def get_result():
    with open('2_items.json') as file:
        products_data = json.load(file)
    with open('4_items_prices.json') as file:
        products_prices = json.load(file)
    products_data = products_data.get('body').get('products')
    for item in products_data:
        product_id = item.get('productId')
        if product_id in products_prices:
            prices = products_prices[product_id]
            item['item_basePrice'] = prices.get('item_basePrice')
            item['item_salePrice'] = prices.get('item_salePrice')
            item['item_bonus'] = prices.get('item_bonus')

    with open('5_results.json', 'w') as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)

    # with open('4_items_prices.json', 'r') as file:
    #     products_prices = json.load(file)
    # products_data = products_data.get('body').get('products')
    # for item in products_prices:
    #     product_id = item.get('productId')
    #     if product_id in products_prices:
    #         prices = products_prices[product_id]
    #     item['item_basePrice'] = prices.get('item_basePrice')
    #     item['item_salePrice'] = prices.get('item_salePrice')
    #     item['item_bonus'] = prices.get('item_bonus')
    # with open('5_result', 'w'):
    #     json.dump(products_data, file, indent=4, ensure_ascii=False)


def main():
    get_data()


if __name__ == "__main__":
    main()
