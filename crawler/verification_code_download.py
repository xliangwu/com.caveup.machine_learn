import time

import requests


def download_pic(folder, url, count=500):
    http_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }

    # train data
    for i in range(count):
        response = requests.get(url, headers=http_header)
        output = "{}\{}.jpg".format(folder, i)
        open(output, "wb").write(response.content)
        print("output:", output)
        time.sleep(3)


if __name__ == '__main__':
    download_pic(folder="C:\\Users\\wuxue\\Pictures\\test", url="http://wenshu.court.gov.cn/User/ValidateCode/9846")
