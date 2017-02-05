# coding=utf-8
'''
实现xml解析。
xmlns会加到解析名之前。
'''
from xml.dom import minidom
import xml.etree.ElementTree as Et
import os
from re import findall

filename = '00B32824B26ABA2D4825809F0021C41D.xml'
if os.name == 'nt':
    filename = "C:\Users\kevinbean\Documents\GitHub\practice\\xml2markdown_30\\00B32824B26ABA2D4825809F0021C41D.xml"

# 使用xml.etree.ElementTree，Python标准库中，提供了ET的两种实现。一个是纯Python实现的xml.etree.ElementTree，另一个是速度更快的C语言实现xml.etree.cElementTree。请记住始终使用C语言实现，因为它的速度要快很多，而且内存消耗也要少很多。如果你所使用的Python版本中没有cElementTree所需的加速模块，你可以这样导入模块
'''try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET'''

tree = Et.parse(filename)
root = tree.getroot()
xmlns = '{'+'http://www.lotus.com/dxl'+'}'


'''
支持通过XPath查找元素
下面是一个使用XPath查找元素的示例：

>>> for elem in tree.iterfind('branch/sub-branch'):
...   print elem.tag, elem.attrib
...
sub-branch {'name': 'subrelease01'}
上面的代码返回了branch元素之下所有tag为sub-branch的元素。接下来查找所有具备某个name属性的branch元素：

>>> for elem in tree.iterfind('branch[@name="release01"]'):
...   print elem.tag, elem.attrib
...
branch {'hash': 'f200013e', 'name': 'release01'}
'''

def xmlfind(item, name = '', node = root):
    if name != '':
        key = xmlns + item + '[@name="' + name + '"]'
    else:
        key = xmlns + item
    for elem in node.iterfind(key):
        return elem

# 邮件标题
subjectNode = xmlfind('item', 'Subject')
subject = subjectNode[0].text
# 邮件发送人
authorNode = xmlfind('item', 'yszz_d')
author = authorNode[0].text
# 是否转发
forwardflagNode = xmlfind('item', 'ForwardFlag')
if forwardflagNode[0].text != '':
    isforward = True
# 收件人
tosomeoneNode = xmlfind('item', 'wdSendToPersonName')
tosomeone = tosomeoneNode[0].text
# 是否有附件，附件文件名
attachNode = xmlfind('item', 'WDAPATTACHMENTINFO')
if attachNode[0].text != '':
    hasattach = True
    attach = findall(pattern=ur"<文件名>(.*)</文件名>", string= attachNode[0].text)
    attachfiles = attach[0].split('|')
# 发送的邮件内容
contentsendNode = xmlfind('item', 'wbnr')
contentsend = ''
# 定位到item下richtext下的par，提取text
if contentsendNode[0][0].text:
    contentsend += contentsendNode[0][0].text + '\n'
print contentsend
# 定位到item下richtext下的par下的break，提取tail
for breakNode in contentsendNode[0][0]:
    contentsend += breakNode.tail + '\n'
print contentsend, '1'
breakNode = xmlfind('break', '', node=contentsendNode[0])
print subjectNode[0].tag, subjectNode[0].text, '2'
# print breakNode[0].tag, breakNode[0].text, '3'
print subject, author, isforward, tosomeone, hasattach, attachfiles[0].encode('utf-8'), xmlfind('item','WDAPATTACHMENTINFO')

mdfile = '--- \n title: {0} \n' \
         'date: {1} \n' \
         'category: {2} \n' \
         'tags: {3} \n' \
         'summary: {4} \n' \
         'authors: {5} \n --- \n' \
         ' {4} \n {6}'\
    .format(subject[:min(32, len(subject))].encode('utf-8'),
            '2010-12-03 10:20', 'OA', '已发送', subject.encode('utf-8'),
            author.encode('utf-8'), contentsend.encode('utf-8'))
print mdfile
with open('test.md', 'w') as fd:
    fd.write(mdfile)
    fd.close()

'''使用xml.dom.minidom
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
'''

