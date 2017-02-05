# coding=utf-8
'''
实现xml解析。
xmlns会加到解析名之前。
'''
import xmltodict
import os

filename = '00B32824B26ABA2D4825809F0021C41D.xml'
if os.name == 'nt':
    filename = "C:\Users\kevinbean\Documents\GitHub\practice\\xml2markdown_30\\00B32824B26ABA2D4825809F0021C41D.xml"

with open(filename) as fd:
    obj = xmltodict.parse(fd.read())

print obj

print obj[u'document'][u'item'][-1][u'text']
print obj[u'document'][u'item'][-7][u'richtext'][u'par']['#text']