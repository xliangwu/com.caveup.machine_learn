import csv
import requests
import time
import re
from bs4 import BeautifulSoup


def crawl_content(url):
    http_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }

    try:
        cookies = {"__jsluid_h": "ec153067397a34fdc97ca710fa557df9",
                   "__jsl_clearance": "1577591965.025|0|iBSsc7VE3mh39AKJHLGQmAOtyh4%3D"}
        response = requests.get(url, headers=http_header, cookies=cookies)
        print(url, ":", response.status_code)
        if response.status_code != 200:
            print(url, "返回代码不是200")
            return

        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        table_ele = soup.find("table", "MsoNormalTable")
        return str(table_ele)
    except BaseException as e:
        print(url, '\t', "无法访问此网站", e)


if __name__ == '__main__':

    all_files = [
                 "ybjhDocPcjgView_guangxi_24.csv",
                 "ybjhDocPcjgView_guizhou_22.csv",
                 "ybjhDocPcjgView_hainan_7.csv",
                 "ybjhDocPcjgView_hebei_26.csv",
                 "ybjhDocPcjgView_heilongjiang_32.csv",
                 "ybjhDocPcjgView_henan_63.csv",
                 "ybjhDocPcjgView_hubei_40.csv",
                 "ybjhDocPcjgView_hunan_75.csv",
                 "ybjhDocPcjgView_jiangsu_62.csv",
                 "ybjhDocPcjgView_jiangxi_48.csv",
                 "ybjhDocPcjgView_jilin_34.csv",
                 "ybjhDocPcjgView_liaoning_22.csv",
                 "ybjhDocPcjgView_neimenggu_27.csv",
                 "ybjhDocPcjgView_ningbo_23.csv",
                 "ybjhDocPcjgView_ningxia_9.csv",
                 "ybjhDocPcjgView_qingdao_4.csv",
                 "ybjhDocPcjgView_qinghai_8.csv",
                 "ybjhDocPcjgView_shaanxi_32.csv",
                 "ybjhDocPcjgView_shandong_75.csv",
                 "ybjhDocPcjgView_shanghai_20.csv",
                 "ybjhDocPcjgView_shanxi_43.csv",
                 "ybjhDocPcjgView_shenzhen_6.csv",
                 "ybjhDocPcjgView_sichuan_63.csv",
                 "ybjhDocPcjgView_tianjin_17.csv",
                 "ybjhDocPcjgView_xiamen_7.csv",
                 "ybjhDocPcjgView_xinjiang_25.csv",
                 "ybjhDocPcjgView_xizang_1.csv",
                 "ybjhDocPcjgView_yunnan_41.csv",
                 "ybjhDocPcjgView_zhejiang_70.csv"]

    for file in all_files:
        area = file.split("_")[1]
        print("process file:{}->{} ".format(file, area))
        contents = []
        with open(file, 'r', newline='', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            index = 0
            for row in reader:
                url = r'http://www.cbirc.gov.cn'+row[0]
                page_content = crawl_content(url)
                contents.append(page_content)
                print(index, "->>>done")
                index = index+1
                time.sleep(3)

            with open("ybjhDocPcjgView_"+area+"_content"+".html", 'w', encoding="utf-8", newline='') as f:
                for content in contents:
                    f.write(content)
                    f.write("\n")
