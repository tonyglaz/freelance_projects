import requests
import json
from config import cookies, headers


def get_data():
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
    # получил данные о планшетах
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
    # material_prices = response.get('body').get('materialPrices')
    # for item in material_prices:
    #     item_id = item.get('price').get('productId')
    #     item_base_price = item.get('price').get('basePrice')
    #     item_sale_price = item.get('price').get('salePrice')
    #     item_bonus = item.get('bonusRubles').get('total')
    #     items_prices[item_id] = {
    #         'item_basePrice': item_base_price,
    #         'item_salePrice': item_sale_price,
    #         'item_bonus': item_bonus
    #     }
    with open('4_items_prices.json', 'w') as file:
        json.dump(items_prices, file, indent=4, ensure_ascii=False)


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
    get_result()


if __name__ == "__main__":
    main()
