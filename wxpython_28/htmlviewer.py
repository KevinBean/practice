# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.html
import urllib


###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(600, 500), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_urlTextCtrl = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_urlTextCtrl.SetMinSize(wx.Size(500, 40))

        bSizer2.Add(self.m_urlTextCtrl, 0, wx.ALL, 5)

        self.m_okButton = wx.Button(self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_okButton, 0, wx.ALL, 5)

        bSizer1.Add(bSizer2, 1, wx.EXPAND, 5)

        self.m_htmlWin = wx.html.HtmlWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                            wx.html.HW_SCROLLBAR_AUTO)
        self.m_htmlWin.SetMinSize(wx.Size(600, 400))
        bSizer1.Add(self.m_htmlWin, 0, wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_urlTextCtrl.Bind(wx.EVT_KEY_DOWN, self.onKeyPress)
        self.m_okButton.Bind(wx.EVT_BUTTON, self.onOkButton)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def onKeyPress(self, event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_RETURN:
            self.OpenUrl()
        event.Skip()

    def onOkButton(self, event):
        event.Skip()

    def OpenUrl(self):
        self.url = self.m_urlTextCtrl.GetValue()
        if str(self.url).startswith("http://"):
            pass
        else:
            self.url = "http://" + self.url
        page = unicode(urllib.urlopen(self.url).read(), "gb2312", "ignore").encode("utf-8", "ignore")
        print self.url
        # self.m_htmlWin.SetPage(page)
        wx.CallAfter(self.m_htmlWin.LoadPage,location =   self.url)


app = wx.App()
frame = MyFrame1(None)
frame.Show()
app.MainLoop()
