import os
import wx

class MyFrame(wx.Frame):
    """We simply derive a new class of Frame."""
    def __init__(self,parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200,100))
        self.control = wx.TextCtrl(self, style = wx.TE_MULTILINE)
        self.CreateStatusBar()

        filemenu = wx.Menu()

        menuOpen = filemenu.Append(wx.ID_OPEN,"&Open", "Open a file")
        menuAbout = filemenu.Append(wx.ID_ABORT, "&About", "Information about this program")
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT, "E&xit","Terminate the program")

        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File")
        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU,self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        self.Show(True)

    def OnAbout(self,e):
        dlg = wx.MessageDialog(self,"A small text editor", "About Sample Editor", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def OnExit(self,e):
        self.Close(True)

    def OnOpen(self,e):
        self.dirname = ''
        dlg = wx.FileDialog(self,"Choose a file",self.dirname, "","*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname,self.filename),'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()


app = wx.App(False)
frame = MyFrame(None, 'Small editor')
app.MainLoop()