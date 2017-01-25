import wx
class ExampleFrame(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title)
        panel = wx.Panel(self)

        #Sizers
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        grid = wx.GridBagSizer(hgap=5,vgap=5)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.quote = wx.StaticText(panel, label = "Your quote", pos = (20,30))
        grid.Add(self.quote,pos=(0,0))

        self.logger = wx.TextCtrl(self,pos=(300,20), size=(200,300),style = wx.TE_MULTILINE|wx.TE_READONLY)

        self.button = wx.Button(self, label="Save",pos=(200,325))
        self.Bind(wx.EVT_BUTTON,self.OnClick,self.button)

        self.lblname = wx.StaticText(self, label ="Your name :",pos =(20,60))
        grid.Add(self.lblname,pos=(1,0))

        self.editname = wx.TextCtrl(self, value = "Enter here your name",pos=(150,60),size =(140,-1))
        grid.Add(self.editname,pos=(1,1))

        self.Bind(wx.EVT_TEXT,self.EvtText,self.editname)
        self.Bind(wx.EVT_CHAR,self.EvtChar,self.editname)

        self.samplelist = ['friends','advertising','web search','Yellow Pages']
        self.lblhear = wx.StaticText(self,label = "How did you hear from us ?",pos=(20,90))
        grid.Add(self.lblhear,pos=(3,0))

        self.edithear = wx.ComboBox(self,pos=(150,90),size=(95,-1),choices=self.samplelist,style=wx.CB_DROPDOWN)
        grid.Add(self.edithear,pos=(3,1))

        self.Bind(wx.EVT_COMBOBOX,self.EvtCombobox,self.edithear)
        self.Bind(wx.EVT_TEXT,self.EvtText,self.edithear)

        #Add Space
        grid.Add((10,40),pos=(2,0))

        # CheckBox
        self.insure = wx.CheckBox(self,label="Do you want Insured Shipment ?", pos = (20,180))
        grid.Add(self.insure,pos=(4,0),span=(1,2),flag=wx.BOTTOM,border=5)

        self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox,self.insure)

        # Radio Boxes
        radioList = ['blue','red','yellow','orange']
        self.rb = wx.RadioBox(self,label="What color would you like ?", pos = (20,210)
                              ,choices = radioList,majorDimension=3,style = wx.RA_SPECIFY_COLS)
        grid.Add(self.rb,pos=(5,0),span=(1,2))

        self.Bind(wx.EVT_RADIOBOX,self.EvtRadioBox,self.rb)

        hSizer.Add(grid,0,wx.ALL,5)
        hSizer.Add(self.logger)
        mainSizer.Add(hSizer,0,wx.ALL,5)
        mainSizer.Add(self.button,0,wx.CENTER)
        self.SetSizerAndFit(mainSizer)
        # self.Show()

    def EvtRadioBox(self,event):
        self.logger.AppendText('EvtRadioBox:%d\n'% event.GetInt())
    def EvtCombobox(self,event):
        self.logger.AppendText('EvtCombobox:%s\n' % event.GetString())
    def OnClick(self,event):
        self.logger.AppendText('Click on object with Id :%d\n' % event.GetId)

    def EvtText(self,event):
        self.logger.AppendText('EvtText:%s\n' % event.GetString())
    def EvtChar(self,event):
        self.logger.AppendText('EvtChar:%s\n' % event.GetKeyCode())
        event.skip()
    def EvtCheckBox(self,event):
        self.logger.AppendText('EvtCheckBox:%d\n' % event.Checked())


app = wx.App(False)
frame = wx.Frame(None, title = "Demo with Notebook")
nb= wx.Notebook(frame)

nb.AddPage(ExampleFrame(nb,"nb1"), "1")
nb.AddPage(ExampleFrame(nb,"nb2"), "2")
nb.AddPage(ExampleFrame(nb, "nb3"), "3")

frame.Show()
app.MainLoop()