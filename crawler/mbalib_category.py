'''
download category from https://wiki.mbalib.com/wiki/MBA%E6%99%BA%E5%BA%93%E7%99%BE%E7%A7%91:%E5%88%86%E7%B1%BB%E7%B4%A2%E5%BC%95
'''
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import csv
import requests
from bs4 import BeautifulSoup
import time


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
            print(i, href, text)
            if str(href).startswith("https://wiki.mbalib.com/wiki/Category"):
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


def category_2_crawler(url, data=[]):
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
        if str(href).startswith("/wiki/Category"):
            print(href, text)
        elif str(href).startswith("/wiki/"):
            data.append((href, text))
        else:
            print("Ignore", href, text)


def pages_crawler():
    http_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }

    host = "https://wiki.mbalib.com"
    url = r'https://wiki.mbalib.com/w/index.php?title=Special%3AAllpages'
    response = requests.get(url, headers=http_header)
    soup = BeautifulSoup(response.text, 'lxml')
    eles = soup.find_all("a")
    links = []
    for i in range(len(eles)):
        ele = eles[i]
        text = ele.get_text()
        if text == "到":
            link = ele['href']
            links.append(link)

    items = []
    for i in range(len(links)):
        print("process :{}->{}".format(i, links[i]))
        page_url = host + links[i]
        response = requests.get(page_url, headers=http_header)
        soup = BeautifulSoup(response.text, 'lxml')
        body_content = soup.find(id="bodyContent")
        page_tables = body_content.find_all('table')
        item_links = page_tables[2].find_all("a")
        for i in range(len(item_links)):
            a_ele = item_links[i]
            text = a_ele.get_text()
            href = a_ele['href']
            print(text, href)
            items.append((text, host + href))

        time.sleep(2)

    # output
    if items:
        with open("mbalib_item.csv", 'w', newline='', encoding='utf-8') as csv_file:
            output = csv.writer(csv_file)
            for i in range(len(items)):
                output.writerow(items[i])


def test():
    http_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }

    page_url = r'https://wiki.mbalib.com/wiki/Special:Allpages/%E5%B9%BF%E5%91%8A%E7%BA%A6%E8%A7%81'
    print(page_url)
    response = requests.get(page_url, headers=http_header)
    soup = BeautifulSoup(response.text, 'lxml')
    body_content = soup.find(id="bodyContent")
    page_tables = body_content.find_all('table')
    links = page_tables[2].find_all("a")
    for i in range(len(links)):
        a_ele = links[i]
        text = a_ele.get_text()
        href = a_ele['href']
        print(text, href)


def csv_test():
    with open("mbalib_level_1.csv", 'w', newline='', encoding='utf-8') as csv_file:
        output = csv.writer(csv_file)
        output.writerow((1, 2, 3))
        output.writerow((11, 22, 33))


if __name__ == '__main__':
    pages_crawler()
    # category_2_cralwer(r'https://wiki.mbalib.com/wiki/Category:%E7%AE%A1%E7%90%86%E7%90%86%E8%AE%BA', [])
