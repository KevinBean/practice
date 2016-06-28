# -*- coding=utf-8 -*-

import io

file = io.open('filtered_words.txt', 'r')
list = []
for word in file.readlines():
    list.append(word.strip('\n'))

print(list)

def isValid(mystr):
    result = mystr
    for x in list:
        if result.find(x) != -1: #判断是否含敏感词
            result = result.replace(x, '**') #哇,这么简单就替换啦!!!
    return result

mystr = input("please input a string:")
print (isValid(mystr))

file.close()