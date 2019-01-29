import requests


def pages_crawler():
    http_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }

    url = r'https://robo.datayes.com/v2/indicator_library'
    response = requests.get(url, headers=http_header)
    print(response.text)


if __name__ == '__main__':
    pages_crawler()
