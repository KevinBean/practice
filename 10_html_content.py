# -*- coding=utf-8 -*-

from bs4 import BeautifulSoup
import io,requests #requests获取网页
file = io.open('Test.html','r')
# 至于io.open，其实是因为Python 2的open实际上是file模块提供的，而Python 3的open是io模块提供的。然后，Python 2.6引入了这个Python 3的特性，叫做io.open，以便和原来的open相区分。
soup = BeautifulSoup(file)
print(soup.getText().strip("\n"))
print(soup.getText())
file.close()

url = 'http://git.writelab.cn/About.html'
html = requests.get(url).content #获取网页内容
file2 = BeautifulSoup(html)
soup2 = file2.getText()
print(soup2)