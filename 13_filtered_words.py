# -*- coding=utf-8 -*-
#还是搞不定中文输入输出!!!
import io

file = io.open('filtered_words.txt','r')
list = []
for word in file.readlines():
    list.append(word.strip('\n'))

print list

myword = raw_input("please input a word:")
'''raw_input() 将所有输入作为字符串看待，返回字符串类型。
而 input() 在对待纯数字输入时具有自己的特性，它返回所输入的数字的类型（ int, float ）；
同时在例子 1 知道，input() 可接受合法的 python 表达式，
举例：input( 1 + 3 ) 会返回 int 型的 4 。'''
if myword in list:
    print "Freedom"
else:
    print "Human Rights"