import requests


def download_pages():
    url_path = 'http://www.mse.fudan.edu.cn/_upload/article/files/8b/57/7d41cdf24c77b31fc8662d7072f2/51a9e523-3724-490c-b106-8d12712df38d_{0}.png'
    http_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }

    for i in range(1, 60):
        url = url_path.format(i)
        response = requests.get(url, headers=http_header)
        if response.status_code == 200:
            print(url, response.status_code)
            with open("D:\资料归类\复旦论文\论文格式\{}.png".format(i), 'wb') as f:
                f.write(response.content)


if __name__ == '__main__':
    download_pages()
