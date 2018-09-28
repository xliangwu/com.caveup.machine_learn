'''
download category from https://wiki.mbalib.com/wiki/MBA%E6%99%BA%E5%BA%93%E7%99%BE%E7%A7%91:%E5%88%86%E7%B1%BB%E7%B4%A2%E5%BC%95
'''
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import csv
import requests
from bs4 import BeautifulSoup


def category_crawler():
    browser = webdriver.Chrome()
    url_level_one = r'https://wiki.mbalib.com/wiki/MBA%E6%99%BA%E5%BA%93%E7%99%BE%E7%A7%91:%E5%88%86%E7%B1%BB%E7%B4%A2%E5%BC%95'

    mbalib_level_1 = []
    try:
        browser.get(url_level_one)
        links = browser.find_elements_by_tag_name("a")

        for i in range(len(links)):
            ele_link = links[i]
            href = ele_link.get_attribute("href")
            text = ele_link.text
            if str(href).startswith("https://wiki.mbalib.com/wiki/Category"):
                print(i, href, text)
                mbalib_level_1.append((i, text, href))
    except TimeoutException:
        print("Cralwer failed")
    finally:
        browser.close()

    # output
    if mbalib_level_1:
        with open("mbalib_level_1.csv", 'w', newline='') as csv_file:
            output = csv.writer(csv_file)
            for i in range(len(mbalib_level_1)):
                output.writerow(mbalib_level_1[i])


def category_2_cralwer(url, data):
    http_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }

    response = requests.get(url, headers=http_header)
    soup = BeautifulSoup(response.text, 'lxml')
    body_content = soup.find(id="bodyContent")
    eles = body_content.find_all("a")
    for i in range(len(eles)):
        ele = eles[i]
        print(ele)
        href = ele['href']
        text = ele.contents
        print(href, text)


def csv_test():
    with open("mbalib_level_1.csv", 'w', newline='', encoding='uft-8') as csv_file:
        output = csv.writer(csv_file)
        output.writerow((1, 2, 3))
        output.writerow((11, 22, 33))


if __name__ == '__main__':
    category_2_cralwer(r'https://wiki.mbalib.com/wiki/Category:%E7%AE%A1%E7%90%86%E7%90%86%E8%AE%BA', [])
