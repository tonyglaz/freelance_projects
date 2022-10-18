import time
from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
useragent = UserAgent()
options.add_argument(f'user-agent={useragent.opera}')  # ie,opera
driver = webdriver.Chrome(
            executable_path=r'D:/Py_projects/scraping/parsing_with_selenium/chromedriver.exe',
            options=options)

def get_data():
    try:
        print('start finding')
        last_page=driver.find_elements(By.XPATH,"//li[@class='page']")[-1].text
        #print(last_page)
        for page_num in range(int(last_page)):
            url = f"https://coinmarketcap.com/?page={page_num+1}"
            driver.get(url)
            for i in range(9):
                js = 'var q = document.documentElement.scrollTop=' + str(i * 1000)
                driver.execute_script(js)  # execute js code
            html_doc=driver.page_source
            soup = BeautifulSoup(html_doc, 'lxml')
            names=soup.find_all('p','sc-14rfo7b-0 lhJnKD')
            del names[0:6]
            for index,item in enumerate(names):
                print(index, '+' ,item.text)
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
        

def main():
    url="https://coinmarketcap.com"
    driver.get(url=url)
    driver.implicitly_wait(3)
    get_data()


if __name__ == '__main__':
    main()