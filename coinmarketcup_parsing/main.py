import requests
from config import headers
from bs4 import BeautifulSoup
from multiprocessing import Pool
import xlsxwriter
import csv
import json
import time


def get_urls():
    url = "https://coinmarketcap.com/all/views/all/"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    data = soup.find_all("tr", class_="cmc-table-row")
    # print(data)
    urls = []

    for i in data:
        print(i)
        res = i.find_all('div',
                         class_='sc-1ibw5f9-0 bpOMHJ cmc-table__column-name cmc-table__column-name--narrow-layout')
        cryptocurrenc_url = f"https://coinmarketcap.com{i.find('a').get('href')}"
        print(cryptocurrenc_url)
        urls.append(cryptocurrenc_url)
    return urls


def run_func(urls):
    for index, currency_url in enumerate(urls):
        # print(index)
        print(currency_url)
        response = requests.get(currency_url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        try:
            name = soup.find('span', class_='sc-169cagi-0 kQxZxB').text
        except:
            name = soup.find('span', class_='sc-169cagi-0 kQxZxB small').text
        price = soup.find('div', class_='priceValue').text
        try:
            price_change = "+" + soup.find('span', class_='sc-15yy2pl-0 feeyND').text
        except:
            price_change = "-" + soup.find('span', class_="sc-15yy2pl-0 gEePkg").text
        market_cap = soup.find('div', class_='statsValue').text
        yield name, price, price_change, market_cap
        # print(f"Название:{name} Цена:{price} Изменение:{price_change} Капитализация на рынке:{market_cap}")
        # time.sleep(1)


def write_to_excel(param):
    book = xlsxwriter.Workbook(r"data.xlsx")
    page = book.add_worksheet("Валюта")

    row, col = 0, 0
    page.set_column("A:A", 20)
    page.set_column("B:B", 20)
    page.set_column("C:C", 20)
    page.set_column("D:D", 20)

    for item in param():
        page.write(row, col, item[0])
        page.write(row, col + 1, item[1])
        page.write(row, col + 2, item[2])
        page.write(row, col + 3, item[3])
        row += 1

    book.close()


def write_to_csv():
    start_time = time.time()
    data = []
    for index, value in enumerate(run_func()):
        # print(index)
        data.append([value[0], value[1], value[2], value[3]])
    # for item in run_func():
    #     data.append([item[0], item[1], item[2], item[3]])
    # print("--- %s seconds ---" % (time.time() - start_time))
    # start_time = time.time()
    with open('data.csv', 'a', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                'Название',
                'Цена',
                'Изменение',
                'Общая капитализация',
            )
        )
        writer.writerows(data)
        # print("--- %s seconds ---" % (time.time() - start_time))


def write_to_json(urls):
    data = {}
    for index, value in enumerate(run_func(urls)):
        data[index] = {
            'Название': value[0],
            'Цена': value[1],
            'Изменение': value[2],
            'Общая капитализация': value[3],
        }
    with open('data.json', 'w', encoding='cp1251') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    start_time = time.time()
    all_links = get_urls()
    #print(all_links)
    # write_to_excel(run_func)
    # write_to_csv()
    # with Pool(10) as p:
    #    p.map(write_to_json, all_links)
    write_to_json(all_links)
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()
