# -*- coding=utf-8 -*-
import io
from bs4 import BeautifulSoup

with io.open('Test.html') as file:
    html = file.read()
    soup = BeautifulSoup(html)
    listA = soup.find_all('a')  #好棒的方法
    listL = soup.find_all('link')
    listI = soup.find_all('img')

    print listA
    print listL
    print listI

for x in listA:
    print(x['href'])
for x in listL:
    print(x['href'])
for x in listI:
    print(x['src'])
