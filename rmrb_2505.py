
import requests
from bs4 import BeautifulSoup
import wget
from PyPDF2 import PdfMerger
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'
}


date_list = pd.date_range("20250513", "20250519").strftime("%Y-%m-%d").tolist()


def get_date(today):
    url = "http://paper.people.com.cn/rmrb/pc/layout/%s%s/%s/node_01.html" % (today[0:4],today[5:7],today[8:10])
    #print(url)
    html = requests.get(url, headers=headers).content
    soup = BeautifulSoup(html, 'lxml')

    pages = soup.find_all(attrs={'class': 'swiper-slide'})
    page_num = len(pages)
    print(today)
    print(page_num)
    merger = PdfMerger()

    f = open('down.txt', 'w', encoding='utf-8')
    for i in range(1, page_num+1):
        link_url = "http://paper.people.com.cn/rmrb/pc/layout/%s%s/%s/node_%02d.html" % (today[0:4],today[5:7],today[8:10],i)
        link_html = requests.get(link_url, headers=headers).content
        link_soup = BeautifulSoup(link_html, 'lxml')
        down_url = link_soup.find_all(attrs={'class': 'right btn'})[0].a['href']
        down_url = down_url.replace("../../..", "http://paper.people.com.cn/rmrb/pc")
        #print(down_url)
        filename = ".\\download\\rmrb%s%s%s%02d.pdf" % (today[0:4],today[5:7],today[8:10],i)
        #print(filename)
        wget.download(down_url, filename)
        merger.append(filename)
        f.write(down_url + "\n")
    f.close()

    merger.write(".\\merged\\rmrb%s%s%s.pdf" % (today[0:4],today[5:7],today[8:10]))
    merger.close()

for riqi in date_list:
    get_date(riqi)




