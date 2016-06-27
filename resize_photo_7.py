# coding=utf-8
# 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小 1136*640。
# python os模块包含普遍的操作系统功能。如果你希望你的程序能够与平台无关的话，这个模块是尤为重要的。即它允许一个程序在编写后不需要任何改动，也不会发生任何问题，就可以在Linux和Windows下运行。
import os
from PIL import Image,ImageDraw,ImageFont
source_dir = raw_input()
#读取目录,获取照片列表,循环处理  /Users/bianbin/PycharmProjects/mengmatest/ins/
source_dir = str(source_dir)
images = os.listdir(source_dir)

#缩放大小
for image in images:
    image_abspath = os.path.join(source_dir, image)  #连接目录与文件名,获得绝对文件路径 if you use os.path.abspath,there may be some error
    print image_abspath
    if (os.path.isfile(image_abspath) & (image.split('.')[1] == 'jpg')):  #os.path.isfile need a abspath 判断name是不是一个jpg文件，不存在name也返回false
        im = Image.open(image_abspath)
        w, h = im.size
        # n = w/600 if (w/600) >= (h/400) else h/400 # if else的用法
        new_im = im.resize((128,128)) #要用一个新名称存储,不然im本身不会有变化 note: the resize returns a resized copy of an image , so you need a new object to save it
        new_im.save('finish_' + image.split('.')[0] + '.jpg', 'jpeg')


"""
第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

from PIL import Image
import os

__author__ = 'Chris5641'


def change_resolution(path):
    for picname in os.listdir(path):
        if picname.split('.')[0] != '':
            picpath = os.path.join(path, picname)
            with Image.open(picpath) as im:
                w, h = im.size
                n = w/136 if (w/136) >= (h/64) else h/64
                im.thumbnail((w/n, h/n))
                im.save('finish_'+picname.split('.')[0]+'.jpg', 'jpeg')


if __name__ == '__main__':
    change_resolution('/Users/bianbin/PycharmProjects/mengmatest/ins/')
"""