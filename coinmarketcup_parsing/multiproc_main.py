import requests
from config import headers
from bs4 import BeautifulSoup
from multiprocessing import Pool
import xlsxwriter
import csv
import json
import time



def get_urls():
    url = "https://coinmarketcap.com"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    dta = soup.find('ul', class_='pagination').text[-2] + soup.find('ul', class_='pagination').text[-1]
    urls = []
    for page_num in range(int(dta)):
        url = f"https://coinmarketcap.com/?page={page_num}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        cryptocurrencies = soup.find("tbody")
        print(cryptocurrencies)
        # https://coinmarketcap.com/?page=2
        # rank=cryptocurrencies.find('p',class_='sc-14rfo7b-0 hueJdC').text
        # print(rank)
        # name=cryptocurrencies.find('p',class_='sc-14rfo7b-0 lhJnKD').text
        # print(name)
        #TODO подгружает первую десятку валют а дальше нет исправить
        for index, cryptocurrency in enumerate(cryptocurrencies):
            print(index)
            if index==11 or index==10:
                continue
            else:
                rank = cryptocurrency.find('p', class_='sc-14rfo7b-0 hueJdC').text
                name = cryptocurrency.find('p', class_='sc-14rfo7b-0 lhJnKD').text
                short_name = cryptocurrency.find('p', class_='sc-14rfo7b-0 emEbFH coin-item-symbol').text
                price = cryptocurrency.find('div', class_='sc-131di3y-0 cLgOOr').text
                try:
                    price_change = '+' + cryptocurrency.find('span', class_='sc-15yy2pl-0 kAXKAX').text
                except:
                    price_change = '-' + cryptocurrency.find('span', class_='sc-15yy2pl-0 hzgCfk').text
                print(rank,name,short_name,price,price_change)
    return urls


def run_func(urls):
    data = {}
    response = requests.get(urls, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    try:
        name = soup.find('span', class_='sc-169cagi-0 kQxZxB').text
    except:
        name = soup.find('span', class_='sc-169cagi-0 kQxZxB small').text
    print(name)
    rank = soup.find('td',
                     class_='cmc-table__cell cmc-table__cell--sticky cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__rank').text
    price = soup.find('div', class_='priceValue').text
    try:
        price_change = "+" + soup.find('span', class_='sc-15yy2pl-0 feeyND').text
    except:
        price_change = "-" + soup.find('span', class_="sc-15yy2pl-0 gEePkg").text
    market_cap = soup.find('div', class_='statsValue').text
    # print(f"Название:{name} Цена:{price} Изменение:{price_change} Капитализация на рынке:{market_cap}")
    # time.sleep(1)
    data[rank] = {
        'Название': name,
        'Цена': price,
        'Изменение': price_change,
        'Общая капитализация': market_cap,
    }
    write_to_json(data)


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


def write_to_json(data):
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    start_time = time.time()
    # print(all_links)
    # write_to_excel(run_func)
    # write_to_csv()
    # write_to_json()
    urls = get_urls()
    # with Pool(10) as p:
    #     p.map(run_func, urls)
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()
