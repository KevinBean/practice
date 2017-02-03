# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import os

###########################################################################
## Class WorkLog
###########################################################################

class WorkLog(wx.Dialog):
    def __init__(self, parent,title,cats,pros):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=title, pos=wx.DefaultPosition,
                           size=wx.Size(950, 500), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        inputSizer = wx.FlexGridSizer(0, 2, 0, 0)
        inputSizer.SetFlexibleDirection(wx.BOTH)
        inputSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_titleLabel = wx.StaticText(self, wx.ID_ANY, u"标题*", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_titleLabel.Wrap(-1)
        inputSizer.Add(self.m_titleLabel, 0, wx.ALL, 5)

        self.m_titleTextCtrl = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_titleTextCtrl.SetMinSize(wx.Size(800, -1))

        inputSizer.Add(self.m_titleTextCtrl, 0, wx.ALL, 5)

        self.m_detailLabel = wx.StaticText(self, wx.ID_ANY, u"详细内容", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_detailLabel.Wrap(-1)
        inputSizer.Add(self.m_detailLabel, 0, wx.ALL, 5)

        self.m_detailTextCtrl = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                            wx.TE_MULTILINE)
        self.m_detailTextCtrl.SetMinSize(wx.Size(800, -1))

        inputSizer.Add(self.m_detailTextCtrl, 0, wx.ALL, 5)

        self.m_dealLabel = wx.StaticText(self, wx.ID_ANY, u"后续处理", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_dealLabel.Wrap(-1)
        inputSizer.Add(self.m_dealLabel, 0, wx.ALL, 5)

        self.m_dealTextCtrl = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                          wx.TE_MULTILINE)
        self.m_dealTextCtrl.SetMinSize(wx.Size(800, -1))

        inputSizer.Add(self.m_dealTextCtrl, 0, wx.ALL, 5)

        self.m_todoLabel = wx.StaticText(self, wx.ID_ANY, u"提醒日期", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_todoLabel.Wrap(-1)
        inputSizer.Add(self.m_todoLabel, 0, wx.ALL, 5)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_todoDatePicker = wx.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                                  wx.DefaultSize, wx.DP_DEFAULT)
        bSizer2.Add(self.m_todoDatePicker, 0, wx.ALL, 5)

        self.m_todoCheckBox = wx.CheckBox(self, wx.ID_ANY, u"是否提醒", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_todoCheckBox, 0, wx.ALL, 5)

        inputSizer.Add(bSizer2, 1, wx.EXPAND, 5)

        self.m_categoryLabel = wx.StaticText(self, wx.ID_ANY, u"分类", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_categoryLabel.Wrap(-1)
        inputSizer.Add(self.m_categoryLabel, 0, wx.ALL, 5)

        m_categoryChoiceChoices = cats
        self.m_categoryChoice = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_categoryChoiceChoices,
                                          0)
        self.m_categoryChoice.SetSelection(0)
        inputSizer.Add(self.m_categoryChoice, 0, wx.ALL, 5)

        self.m_projectLabel = wx.StaticText(self, wx.ID_ANY, u"工程项目", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_projectLabel.Wrap(-1)
        inputSizer.Add(self.m_projectLabel, 0, wx.ALL, 5)

        m_projectChoiceChoices = pros
        self.m_projectChoice = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_projectChoiceChoices, 0)
        self.m_projectChoice.SetSelection(0)
        inputSizer.Add(self.m_projectChoice, 0, wx.ALL, 5)

        self.m_labelLabel = wx.StaticText(self, wx.ID_ANY, u"标签", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_labelLabel.Wrap(-1)
        inputSizer.Add(self.m_labelLabel, 0, wx.ALL, 5)

        self.m_tagText = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_tagText.SetMinSize(wx.Size(800, -1))

        inputSizer.Add(self.m_tagText, 0, wx.ALL, 5)

        bSizer1.Add(inputSizer, 1, wx.EXPAND, 5)

        buttonSizer = wx.BoxSizer(wx.HORIZONTAL)

        buttonSizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        self.m_buttonClose = wx.Button(self, wx.ID_ANY, u"关闭", wx.DefaultPosition, wx.DefaultSize, 0)
        buttonSizer.Add(self.m_buttonClose, 0, wx.ALL, 5)

        self.m_buttonLog = wx.Button(self, wx.ID_ANY, u"记录", wx.DefaultPosition, wx.DefaultSize, 0)
        buttonSizer.Add(self.m_buttonLog, 0, wx.ALL, 5)

        bSizer1.Add(buttonSizer, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_categoryChoice.Bind(wx.EVT_CHOICE, self.EvtCategory)
        self.m_projectChoice.Bind(wx.EVT_CHOICE, self.EvtProject)
        self.m_buttonClose.Bind(wx.EVT_BUTTON, self.EvtClose)
        self.m_buttonLog.Bind(wx.EVT_BUTTON, self.EvtLog)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def EvtCategory(self, event):
        event.Skip()

    def EvtProject(self, event):
        event.Skip()

    def EvtClose(self, event):
        self.Close()

    def EvtLog(self, event):
        title = self.m_titleTextCtrl.Value
        detail = self.m_dealTextCtrl.Value
        deal = self.m_dealTextCtrl.Value
        todoBoolean = self.m_todoCheckBox.Value
        todoDate = self.m_todoDatePicker.Value
        cat = cats[self.m_categoryChoice.CurrentSelection]
        pro = pros[self.m_projectChoice.CurrentSelection]
        tags = self.m_tagText.Value + ',' + cat + ',' + pro
        if todoBoolean:
            tags += ',todo'

        import socket
        # 获取本机电脑名
        myname = socket.getfqdn(socket.gethostname())

        log = "Title: %s\n" \
              " Date: %s\n" \
              " Category: %s\n" \
              " Tags: %s\n" \
              " Authors: %s\n" \
              " Summary: %s\n" \
              "#%s\n" \
              "%s\n" \
              "%s\n" % (title,todoDate,cat,tags,myname,detail,title,detail,deal)

        self.logfilename=title + '.md'
        dirname = os.path.curdir + os.sep + 'log'
        if os.path.exists(dirname):
            pass
        else:
            os.mkdir(dirname)
        f = open(dirname + os.sep + self.logfilename,'w')
        f.write(log.encode('utf-8'))
        f.close()
        self.Close()

        print title,todoBoolean,todoDate,tags


app = wx.App(False)
cats = [u'计划内',u'计划外']
pros = [u'无','B']
frame = WorkLog(None, u'工作记录',cats,pros)
frame.Show(True)
app.MainLoop()