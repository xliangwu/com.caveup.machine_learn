import csv

import requests
from bs4 import BeautifulSoup


def pages_crawler(url):
    http_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }

    try:
        response = requests.get(url, headers=http_header)
        if response.status_code != 200:
            print(url, "无法访问此网站")
            return
        response_encoding = response.encoding
        response_decoding = 'UTF-8'
        html = response.text
        content_type = response.headers.get('Content-Type')
        if 'charset' in content_type:
            response_decoding = str(content_type).split("=")[1]

        if response_encoding != 'UTF-8':
            try:
                html = html.encode(response_encoding)
                html = html.decode(response_decoding)
            except BaseException as e:
                html = html.decode("gb2312")

        soup = BeautifulSoup(html, 'lxml')
        eles = soup.find_all("meta")
        desc_found = False
        for i in range(len(eles)):
            ele = eles[i]
            ele_name = ele.get("name")
            if ele_name and str(ele_name).lower() == 'description':
                print(url, '\t', ele.get("content"))
                desc_found = True

        if not desc_found:
            print(url, '\t', "没有描述")

    except BaseException as e:
        print(url, '\t', "无法访问此网站", e)


def sentiment_net_crawler():
    with open("sentiment_net.csv", 'r', newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        i = 0
        for row in reader:
            # print("{}:processing {}".format(i, row[0]))
            pages_crawler("http://" + row[0])
            i += 1


if __name__ == '__main__':
    # pages_crawler(r'http://orz520.com')
    sentiment_net_crawler()
