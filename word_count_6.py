# coding=utf-8
# 任一个英文的纯文本文件，统计其中的单词出现的个数。
# 我的解法,用nltk
import nltk
#FreqDist要从nltk.book中导入
from nltk.book import *
#读取文本,分词
def howmany(word):
    f = open('document.txt')
    raw = f.read()
    tokens = nltk.word_tokenize(raw)
    #分词后,要编程nltk中指定的text格式
    text = nltk.Text(tokens)
    print len(set(text))
    print len(text)
    print len(tokens)
    #统计词频
    fdist = FreqDist(text)
    return fdist[word]
if __name__ == '__main__':
    print howmany('you')

# 另一种手动解法,用正则表达式,搜索字符后计数
# python通过re模块提供对正则表达式的支持
import re
fin=open("document.txt","r")
fout=open("result.txt","w")
str=fin.read()
#匹配正则表达式
reObj=re.compile("\b?([a-zA-Z]+)\b?")
words=reObj.findall(str)
#建立空字典
word_dict={}
#以单词的小写作为键值进行统计，同时要
for word in words:
    if(word_dict.has_key(word)):
        word_dict[word.lower()]=max(word_dict[word.lower()],words.count(word.lower())+words.count(word.upper())+words.count(word))
    else:
        word_dict[word.lower()]=max(0,words.count(word.lower())+words.count(word.upper())+words.count(word))
for(word,number) in word_dict.items():
    fout.write(word+":%d\n"%number)


# 另一种解法?但似乎只是统计了字数?.用split在空格处分隔原始文本
    def count():
        name = raw_input("Enter file:")
        if len(name) < 1: name = "test.txt"
        handle = open(name)
        # raw = handle.read()
        count_words = list()
        for line in handle:
            count_words += line.split()
        # print len(raw.split())
        return len(count_words)

    print count()

