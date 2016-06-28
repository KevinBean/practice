# -*- coding=utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re
import urllib

my_url = "http://tieba.baidu.com/p/2166231880"

def get_img_list(url):
    html = requests.get(url).content #获取网页内容
    soup = BeautifulSoup(html, "html5lib")
    list = soup.find_all('img')  # 好棒的方法
    return list

def get_img(list):
    for x in list:
        src = x['src']
        if 'jpg' in src:
            urllib.urlretrieve(src, src[-8:-4]+'.jpg') #urllib.urlretrieve() 下载文件

print get_img(get_img_list(my_url))

