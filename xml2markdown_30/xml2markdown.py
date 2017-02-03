# coding=utf-8
'''

'''
from xml.dom import minidom

def get_nodevalue(node , index = 0):
    return node.childNodes[index].nodeValue if node else ''

def get_xmlnode(node,name):
    return node.getElementsByTagName(name) if node else ''

# 加载读取xml文件
doc = minidom.parse("C:\Users\kevinbean\Documents\GitHub\practice\\xml2markdown_30\\00B32824B26ABA2D4825809F0021C41D.xml")
# 获取xml文档对象
root = doc.documentElement
node_subject = get_xmlnode(root,'document')
print node_subject[0]
subject = get_xmlvalue(node_subject[0])

print subject


