import time
import json
from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from multiprocessing import Pool
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
useragent = UserAgent()
options.add_argument(f'user-agent={useragent.opera}')  # ie,opera
#options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--disable-blink-features=AutomationControlled')


def get_data(url):
    try:
        driver = webdriver.Chrome(
            executable_path=r'D:\Py_projects\freelance_projects\Dubai_parsing_dxbinteract\chromedriver-win64\chromedriver.exe',
            options=options)
        driver.get(url)
        for i in range(10):
            js = 'var q = document.documentElement.scrollTop=' + str(i * 1100)
            driver.execute_script(js)  # execute js code
        html_doc = driver.page_source
        #print(url)
        soup = BeautifulSoup(html_doc, 'lxml')
        volumes = soup.find_all('p', 'sc-14rfo7b-0 fVSMmK font_weight_500')
        # for index,item in enumerate(volumes):
        #     print(index,item.text)
        names = soup.find_all('p', 'sc-14rfo7b-0 lhJnKD')
        prices = soup.find_all('div', 'sc-131di3y-0 cLgOOr')
        market_caps = soup.find_all('span', 'sc-1ow4cwt-1 ieFnWP')
        del names[0:6], prices[0:3]
        page_num = url.split('=')[1]
        data = {}
        for index, (volume, name, price, cap) in enumerate(zip(volumes, names, prices, market_caps)):
            data[index] = {
                'Название': name.text,
                'Цена': price.text,
                'Общая капитализация': cap.text,
                'Объем': volume.text,
            }
        with open(f'pages/pageNum_{page_num}.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
            # print(
            #     f'{index} \t rank:{rank.text}\tname:{name.text}\t price:{price.text}\t cap:{cap.text}')
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
        # TODO подключить мультипоток,сделать быструю запись в файлы,парсить не только имя но и остальные данные
        # настроить цвет комментов в vs code^)

def main():
    start_time = time.time()
    driver = webdriver.Chrome()
    try:
        service = Service(executable_path=r'D:\Py_projects\freelance_projects\Dubai_parsing_dxbinteract\chromedriver-win64\chromedriver.exe')
        driver = webdriver.Chrome(
            options=options,
            service=service
        )
        url = "https://dxbinteract.com/dubai-house-prices/business-bay"
        driver.get(url=url)
        driver.maximize_window()  # For maximizing window
        driver.implicitly_wait(20)  # gives an implicit wait for 20 seconds
        driver.get(url=url)
        #time.sleep(10)
        driver.find_element(By.XPATH, "/ *[ @ id = ""t_Alert_Notification""] / div / div[3] / button").click()
        time.sleep(4)
        driver.find_element(By.XPATH, "// *[ @ id = ""t_PageBody""] / div[3] / div[3] / div / button").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//*[@id=""8432884779403949182""]/li[2]/a").click()

        time.sleep(5)
        last_page = int(driver.find_elements(
            By.XPATH, "//li[@class='page']")[-1].text)
        urls_list = [
            f"https://coinmarketcap.com/?page={int(page)+1}" for page in range(16)]
        print(urls_list)
        #get_data(f"https://coinmarketcap.com/?page={5}")
        p = Pool(processes=8)
        p.map(get_data, urls_list)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()

