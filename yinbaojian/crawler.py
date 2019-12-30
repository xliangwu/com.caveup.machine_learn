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
                   "__jsl_clearance": "1577502063.439|0|cnvongdHKKLqNObgw0ZI9JOW3B4%3D"}
        response = requests.get(url, headers=http_header, cookies=cookies)
        print(response.status_code)
        if response.status_code != 200:
            print(url, "返回代码不是200")
            return

        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        table_ele = soup.find("table", "MsoNormalTable")
        htmlContent = str(table_ele)
    except BaseException as e:
        print(url, '\t', "无法访问此网站", e)


def crawer_all_links(url):
    http_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }
    all_links = []
    try:
        cookies = {"__jsluid_h": "1ab28b6e9a8e92d1f9339484b5a93de2",
                   "__jsl_clearance": "1577467487.227|0|PtNp46n8hvJ9xngwfXcP9JTxrKc%3D"}
        response = requests.get(url, headers=http_header, cookies=cookies)
        print(response.status_code)
        if response.status_code != 200:
            print(url, "返回代码不是200")
            return

        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        eles = soup.find_all("td", "dotbg")
        for i in range(len(eles)):
            ele = eles[i]
            linkEle = ele.find("a")
            all_links.append([linkEle['href']])

    except BaseException as e:
        print(url, '\t', "无法访问此网站", e)
        []

    return all_links
# 采集所有省市的处罚链接


def crawl_links():
    pass

# 采集url的最后一个分页


def crawl_link_end_number(url):
    http_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }

    try:
        cookies = {"__jsluid_h": "ec153067397a34fdc97ca710fa557df9",
                   "__jsl_clearance": "1577459316.89|0|0V1z4%2BXGKA6ojH%2F%2BG9wypRBSbOY%3D"}
        response = requests.get(url, headers=http_header, cookies=cookies)
        if response.status_code != 200:
            print(url, "返回代码不是200")
            return

        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        page_eles = soup.find_all("a", href=re.compile("current"))
        last_page = page_eles[1]
        href = last_page['href']
        end_number = href.split("=")[1]
        return end_number
    except BaseException as e:
        print(url, "->无法访问此网站", e)

    return -1


def crawl_page_links():
    with open("D:\python\project_workspace\com.caveup.machine_learn\yinbaojian\links.csv", 'r', newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            end_number = crawl_link_end_number(row[0])
            print(row[0], end_number)


if __name__ == '__main__':
    # net_crawler("http://www.cbirc.gov.cn/cn/list/9103/910305/ybjhcf/{}.html",1,1)
    # crawer_all_links("http://www.cbirc.gov.cn/zhuanti/xzcf/getYbjhPcjgXZCFDocListDividePage/beijing.html?current=1")
    crawl_content(
        "http://www.cbirc.gov.cn/beijing/ybjhDocPcjgView/05B45037F7B04151907D80DA601EE0A7/26.html")

    # crawl_link_end_number('http://www.cbirc.gov.cn/zhuanti/xzcf/getYbjhPcjgXZCFDocListDividePage/hebei.html?current=2')

    # with open("D:\python\project_workspace\com.caveup.machine_learn\yinbaojian\links_v2_01.csv", 'r', newline='', encoding='utf-8') as csv_file:
    #     reader = csv.reader(csv_file)

    #     for row in reader:
    #        link = row[0]
    #        end_number = row[1]
    #        f = link.split("/")[-1]
    #        area =  f.split(".")[0]
    #        all_links = []
    #        for i in range(1,int(end_number)):
    #            url = link+ "?current="+str(i)
    #            print(url)
    #            page_links = crawer_all_links(url)
    #            all_links = all_links+page_links
    #            time.sleep(3)
    #        with open("ybjhDocPcjgView_"+area+"_"+str(i)+".csv",'w', newline='') as f:
    #            writer = csv.writer(f)
    #            writer.writerows(all_links)

    #        time.sleep(5)

    #     print(all_links)
