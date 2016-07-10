# -*- coding=utf-8 -*-
'''本文实例展示了一个python的tkinter布局的简单聊天窗口。分享给大家供大家参考之用。具体方法如下：
该实例展示的是一个简单的聊天窗口，可以实现下方输入聊天内容，点击发送，可以增加到上方聊天记录列表中。现在只是“单机”版。
右侧预留了空位可以放点儿其它东西。感兴趣的读者可以进一步做成socket双方互聊。
最简单的用法
import Tkinter

root=Tkinter.Tk()  %创建主窗体
MainLabel=Tkinter.Label(root,text="I am so ugly. -- Tkinter",font="Times 16 bold")  %创建元件
MainLabel.pack()  %显示元件
root.mainloop()  %进入窗体的主循环
'''
from Tkinter import *
import datetime
import time

root = Tk() # 创建主窗体
root.title(unicode('与xxx聊天中','utf-8'))

#发送按钮事件
def sendmessage():
    msg = text_msg.get() # 获取输入框信息
    #在聊天内容上方加一行 显示发送人及发送时间
    if msg:
        msgcontent = unicode('我:', 'utf-8') + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n '
        text_msglist.insert(END, msgcontent, 'green')
        text_msglist.insert(END, msg + '\n')
        text_msg.delete(0, END)
    else:
        pass


#创建几个frame作为容器
frame_top   = Frame(width=380, height=270, bg='red')
# frame_left_center  = Frame(width=380, height=100, bg='yellow')
frame_left_bottom  = Frame(width=300, height=30)
frame_right_bottom  = Frame(width=80, height=30)
#frame_right     = Frame(width=170, height=400, bg='white')

##创建需要的几个元素
text_msglist    = Text(frame_top)
text_msg      = Entry(frame_left_bottom);
button_sendmsg   = Button(frame_right_bottom, text=unicode('发送','utf-8'), command=sendmessage)

#创建一个绿色的tag
text_msglist.tag_config('green', foreground='#008B00')

#使用grid设置各个容器位置
frame_top.grid(row=0, column=0, padx=2, pady=5,columnspan=2)
# frame_left_center.grid(row=1, column=0, padx=2, pady=5)
frame_left_bottom.grid(row=1, column=0)
frame_right_bottom.grid(row=1, column=1, padx=4, pady=5)
frame_top.grid_propagate(0)
frame_left_bottom.grid_propagate(0)
frame_right_bottom.grid_propagate(0)

#把元素填充进frame
text_msglist.grid()
text_msg.grid()
button_sendmsg.grid(sticky=E)

#主事件循环
root.mainloop()