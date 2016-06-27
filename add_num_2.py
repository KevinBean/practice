# coding=utf-8
from PIL import Image,ImageDraw,ImageFont

def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('/Library/Fonts/Arial.ttf',size=30) #Mac的字体存储在"应用程序--字体册",也可只写字体名称
    fillcolor = '#ff0000' #也可直接写成red
    width, height = img.size
    draw.text((width-40,0),'99',font=myfont,fill=fillcolor)
    img.save('result.png','png')

    return 0
if __name__ == '__main__':
    image = Image.open('ascii_dora.png')
    add_num(image)

'''
+def add_num(filePath, num=1):
 +    img = Image.open(filePath)
 +    size = img.size
 +    fontsize = size[1]/4
 +    myfont = ImageFont.truetype('Futura.ttf', fontsize)
 +    ImageDraw.Draw(img).text((2 * fontsize, 0), str(num), font = myfont, fill = 'red')
 +    img.save('avatar_added.jpg')
 +    img.show()
 '''