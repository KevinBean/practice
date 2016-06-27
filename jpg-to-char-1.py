# coding=utf-8
''' 加'coding=utf-8'是为了能使用中文注释,不然会报错'SyntaxError: Non-ASCII character '\xef' in file 。。。' '''
from PIL import Image
# 使用的库是pillow,图像处理库

# 命令行参数工具 argparse 给函数加命令行参数
# 此处不是重点，故而不做讲解，具体参见 (https://docs.python.org/2/library/argparse.html)'''

import argparse
parser = argparse.ArgumentParser()

parser.add_argument('file')
parser.add_argument('-o','--output')
parser.add_argument('--width', type = int, default = 80)
parser.add_argument('--height', type = int, default = 80)

# 加入以上语句后,调用参数时的格式就变成了 python jpg-to-char-1.py insta2.jpg -o output.txt --width 160 --height 160

# 以下是从输入读取数据
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output
'''
IMG = 'ascii_dora.png'
WIDTH = 80
HEIGHT = 80
OUTPUT = ''
'''

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
def get_char(r,g,b,alpha = 256):
    # type: (object, object, object, object) -> object
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b) #灰度转换公式
    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':

    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT),Image.NEAREST)

    txt =""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i))) 
        txt += '\n'
    # 可用*im.getpixel((j,i))[:3]来切片r,g,b参数
    
    print txt


    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)