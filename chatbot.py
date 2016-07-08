# -*- coding=utf-8 -*-

import aiml

# 创建Kernel()和 AIML 学习文件
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

# 按组合键 CTRL-C 停止循环
while True:
    print kernel.respond(raw_input("Enter your message >> "))