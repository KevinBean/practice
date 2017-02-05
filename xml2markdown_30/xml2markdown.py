# coding=utf-8
'''
实现xml解析。
xmlns会加到解析名之前。
'''
from xml.dom import minidom
import xml.etree.ElementTree as Et
import os
import time
from re import findall

xmlns = '{' + 'http://www.lotus.com/dxl' + '}'


def xmlfind(tag, node, name=''):
    if name != '':
        key = xmlns + tag + '[@name="' + name + '"]'
    else:
        key = xmlns + tag
    for elem in node.iterfind(key):
        return elem


def readnode(node):
    text = ''
    if node is not None:
        for item in node.iter():
            if item.text:
                text += item.text
            if item.tail:
                text += item.tail
    return text

def xml2md(filename):
    '''
    filename = '00B32824B26ABA2D4825809F0021C41D.xml'
    if os.name == 'nt':
        filename = "C:\Users\kevinbean\Documents\GitHub\practice\\xml2markdown_30\\00B32824B26ABA2D4825809F0021C41D.xml"
    '''
    # 使用xml.etree.ElementTree，Python标准库中，提供了ET的两种实现。一个是纯Python实现的xml.etree.ElementTree，另一个是速度更快的C语言实现xml.etree.cElementTree。请记住始终使用C语言实现，因为它的速度要快很多，而且内存消耗也要少很多。如果你所使用的Python版本中没有cElementTree所需的加速模块，你可以这样导入模块
    '''try:
        import xml.etree.cElementTree as ET
    except ImportError:
        import xml.etree.ElementTree as ET'''

    tree = Et.parse(filename)
    root = tree.getroot()

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
    # 分类
    category = 'OA'

    tags = u''
    date = '2017-02-05 13:59'
    # 时间 格式20170105T140848,93+08
    datesendNode = xmlfind('item', root,  'wdCreated')
    datereceiveNode = xmlfind('item', root, 'DeliveredDate')
    if datesendNode is not None:
        datesend = datesendNode[0].text
        timeformat = time.strptime(datesend[:14], '%Y%m%dT%H%M%S')
        date = time.strftime('%Y-%m-%d %H:%M', timeformat)
        tags = '发件箱'
    if datereceiveNode is not None:
        datereceive = datereceiveNode[0].text
        timeformat = time.strptime(datereceive[:14], '%Y%m%dT%H%M%S')
        date = time.strftime('%Y-%m-%d %H:%M', timeformat)
        tags = '收件箱'
    print date

    # 收到的邮件内容html
    htmlbodyNode = xmlfind('item', root, 'HTMLBody')
    contentreceivehtml = readnode(htmlbodyNode)
    print contentreceivehtml, '1'

    # 邮件标题
    subjectNode = xmlfind('item', root, 'Subject')
    subject = subjectNode[0].text

    # 邮件发送人
    authorNode = xmlfind('item', root, 'yszz_d')
    author = authorNode[0].text

    # 是否转发,暂时无用
    forwardflagNode = xmlfind('item', root, 'ForwardFlag')
    if forwardflagNode[0].text != '':
        isforward = True

    # 收件人，暂时无用
    tosomeoneNode = xmlfind('item', root, 'wdSendToPersonName')
    tosomeone = tosomeoneNode[0].text

    # ID
    idxmlNode = xmlfind('item', root, 'ID')
    idxml = idxmlNode[0].text
    emailfilespath = '/emailfiles/' + idxml + '.xml.files/$file/'

    # 是否有附件，附件文件名
    attachNode = xmlfind('item', root, 'WDAPATTACHMENTINFO')
    attachfiles = []
    hasattach = False
    if attachNode[0].text is not None:
        hasattach = True
        print attachNode[0].text
        attach = findall(pattern=ur"<文件名>(.*)</文件名>", string=attachNode[0].text)
        attachfiles = attach[0].split('|')
    attachhtml = '<br> 附件： <br>'
    for item in attachfiles:
        filepath = emailfilespath + item
        attachhtml += '<a href="{0}">{1}</a><br>'.format(filepath.encode('utf-8'), item.encode('utf-8'))
    print '798', attachhtml, '798'

    contenthtml = contentreceivehtml

    # 发送的邮件内容，暂时无用
    contentsendNode = xmlfind('item', root, 'wbnr')
    contentsend = readnode(contentsendNode)
    '''
    if contentsendNode is not None:
        # 定位到item下richtext下的par，提取text
        if contentsendNode[0][0].text:
            contentsend += contentsendNode[0][0].text + '\n'
        print contentsend
        # 定位到item下richtext下的par下的break，提取tail
        for breakNode in contentsendNode[0][0]:
            contentsend += breakNode.tail + '\n'
        print contentsend, '1'
    '''

    # 发送的邮件内容html
    contentsendhtmlNode = xmlfind('item', root, 'htmlnr1')
    contentsendhtml = readnode(contentsendhtmlNode)
    '''
    contentsendhtml = u''
    if contentsendhtmlNode is not None:
        for item in contentsendhtmlNode.iter():
            if item.text:
                contentsendhtml += item.text
            if item.tail:
                contentsendhtml += item.tail
        print contentsendhtml
    '''


    mdfile = '--- \n Title: {0} \n' \
             'Slug: id-{9} \n' \
             'Date: {1} \n' \
             'Category: {2} \n' \
             'Tags: {3} \n' \
             'Summary: {4} \n' \
             'Authors: {5} \n --- \n' \
             ' {4} \n {8} {6} {7}' \
        .format(subject[:min(32, len(subject))].encode('utf-8'),
                date, category, tags, subject.encode('utf-8'),
                author.encode('utf-8'), contentsendhtml.encode('utf-8'),
                contentreceivehtml.encode('utf-8'), attachhtml, idxml)
    print mdfile
    if os.path.exists('md'):
        pass
    else:
        os.mkdir('md')
    with open('md/' + idxml + '.md', 'w') as fd:
        fd.write(mdfile)
        fd.close()

if __name__ == "__main__":
    list_dirs = os.walk('xml')
    for root, dirs, files in list_dirs:
        for f in files:
            filename = os.path.join(root, f)
            print filename
            if filename[-4:] == '.xml':
                xml2md(filename)


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

