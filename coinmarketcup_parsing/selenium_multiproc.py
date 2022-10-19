import time
from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from multiprocessing import Pool

options = webdriver.ChromeOptions()
useragent = UserAgent()
options.add_argument(f'user-agent={useragent.opera}')  # ie,opera
#options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--disable-blink-features=AutomationControlled')

def get_data(url):
    try:
        driver = webdriver.Chrome(
            executable_path=r'D:/Py_projects/scraping/parsing_with_selenium/chromedriver.exe',
    options=options)
        driver.get(url)
        for i in range(10):
            js = 'var q = document.documentElement.scrollTop=' + \
                str(i * 1100)
            driver.execute_script(js)  # execute js code
        html_doc = driver.page_source
        print(url)
        soup = BeautifulSoup(html_doc, 'lxml')
        names = soup.find_all('p', 'sc-14rfo7b-0 lhJnKD')
        prices=soup.find_all('div', 'sc-131di3y-0 cLgOOr')
        market_caps = soup.find_all('span', 'sc-1ow4cwt-1 ieFnWP')
        del names[0:6],prices[0:3],
        for index,(name,price,cap) in enumerate(zip(names,prices,market_caps)):
            print(f'{index} \t name:{name.text}\t price:{price.text}\t cap:{cap.text}')
        # all_names=driver.find_elements(By.XPATH,"//p[@class='sc-14rfo7b-0 lhJnKD']")
        # print(page_num+1)
        # for index,item in enumerate(all_names):
        #     if index>6:
        #         print(index,item.text)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

        # TODO подключить мультипоток,сделать быструю запись в файлы,парсить не только имя но и остальные данные
        # настроить цвет комментов в vs code^)


def main():
    try:
        driver = webdriver.Chrome(
            executable_path=r'D:/Py_projects/scraping/parsing_with_selenium/chromedriver.exe',
            options=options)
        url = "https://coinmarketcap.com"
        driver.get(url=url)
        last_page = int(driver.find_elements(
            By.XPATH, "//li[@class='page']")[-1].text)
        urls_list = [
            f"https://coinmarketcap.com/?page={int(page)+1}" for page in range(last_page)]
        print(urls_list)
        get_data('https://coinmarketcap.com/?page=2')
       # p = Pool(processes=4)
       # p.map(get_data, urls_list)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    main()
