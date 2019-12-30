import csv
import re
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def crawl_content(url):
    try:
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get(url)
        try:

            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "MsoNormalTable"))
            )
            table_ele = driver.find_element_by_class_name("MsoNormalTable")
            print(table_ele.text)
            return table_ele.get_attribute('outerHTML')
        finally:
            driver.quit()
    except BaseException as e:
        print(url, '\t', "无法访问此网站", e)
    return ""


if __name__ == '__main__':

    all_files = [
        "ybjhDocPcjgView_hainan_7.csv",
        "ybjhDocPcjgView_guangxi_24.csv",
        "ybjhDocPcjgView_guizhou_22.csv",
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
        "ybjhDocPcjgView_ningbo_23.csv"]

    for file in all_files:
        area = file.split("_")[1]
        print("process file:{}->{} ".format(file, area))
        contents = []
        with open("../" + file, 'r', newline='', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            index = 0
            for row in reader:
                if (len(row)) <= 0:
                    break
                if(index>=180):
                    break

                url = r'http://www.cbirc.gov.cn' + row[0]
                page_content = crawl_content(url)
                contents.append(page_content)
                print(index, "->>>done")
                index = index + 1
                time.sleep(2)

            with open("ybjhDocPcjgView_" + area + "_content" + ".html", 'w', encoding="utf-8", newline='') as f:
                for content in contents:
                    f.write(content)
                    f.write("\n")
