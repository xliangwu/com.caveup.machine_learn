import requests


def parse_cookies():
    url = "http://wenshu.court.gov.cn/List/List?sorttype=1&conditions=searchWord+++2018-09-18%20TO%202018-09-19+%E4%B8%8A%E4%BC%A0%E6%97%A5%E6%9C%9F:2018-09-18%20TO%202018-09-19&conditions=searchWord+2+AJLX++%E6%A1%88%E4%BB%B6%E7%B1%BB%E5%9E%8B:%E5%88%91%E4%BA%8B%E6%A1%88%E4%BB%B6"

    http_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Host': 'wenshu.court.gov.cn'
    }

    response = requests.get(url, headers=http_header)
    cookies = response.cookies
    print(cookies)


if __name__ == '__main__':
    parse_cookies()
